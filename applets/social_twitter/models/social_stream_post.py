# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import requests

from tele import models, fields
from tele.http import request
from werkzeug.urls import url_join


class SocialStreamPostTwitter(models.Model):
    _inherit = 'social.stream.post'

    twitter_tweet_id = fields.Char('Twitter Tweet ID', index=True)
    twitter_author_id = fields.Char('Twitter Author ID')
    twitter_screen_name = fields.Char('Twitter Screen Name')
    twitter_profile_image_url = fields.Char('Twitter Profile Image URL')
    twitter_likes_count = fields.Integer('Twitter Likes')
    twitter_user_likes = fields.Boolean('Twitter User Likes')
    twitter_comments_count = fields.Integer('Twitter Comments')
    twitter_retweet_count = fields.Integer('Re-tweets')

    def _compute_author_link(self):
        twitter_posts = self._filter_by_media_types(['twitter'])
        super(SocialStreamPostTwitter, (self - twitter_posts))._compute_author_link()

        for post in twitter_posts:
            post.author_link = 'https://twitter.com/intent/user?user_id=%s' % post.twitter_author_id

    def _compute_post_link(self):
        twitter_posts = self._filter_by_media_types(['twitter'])
        super(SocialStreamPostTwitter, (self - twitter_posts))._compute_post_link()

        for post in twitter_posts:
            post.post_link = 'https://www.twitter.com/%s/statuses/%s' % (post.twitter_author_id, post.twitter_tweet_id)

    # ========================================================
    # COMMENTS / LIKES
    # ========================================================

    def _twitter_comment_add(self, stream, comment_id, message):
        self.ensure_one()
        tweet_id = comment_id or self.twitter_tweet_id
        message = self.env["social.live.post"]._remove_mentions(message)
        params = {
            'status': message,
            'in_reply_to_status_id': tweet_id,
            'tweet_mode': 'extended',
        }

        attachment = None
        files = request.httprequest.files.getlist('attachment')
        if files and files[0]:
            attachment = files[0]

        if attachment:
            images_attachments_ids = stream.account_id._format_bytes_to_images_twitter(attachment)
            if images_attachments_ids:
                params['media_ids'] = ','.join(images_attachments_ids)

        post_endpoint_url = url_join(self.env['social.media']._TWITTER_ENDPOINT, "/1.1/statuses/update.json")
        headers = stream.account_id._get_twitter_oauth_header(
            post_endpoint_url,
            params=params
        )
        result = requests.post(
            post_endpoint_url,
            data=params,
            headers=headers,
            timeout=5
        )

        tweet = result.json()

        formatted_tweet = self.env['social.media']._format_tweet(tweet)

        return formatted_tweet

    def _twitter_comment_fetch(self, page=1):
        """ As of today (07/2019) Twitter does not provide an endpoint to get the 'answers' to a tweet.
        This is why we have to use a quite dirty workaround to try and recover that information.

        Basically, what we do if fetch all tweets that are:
            - directed to our user ('to': twitter_screen_name)
            - are after out tweet_id ('since_id': twitter_tweet_id)

        We accumulate up to 1000 tweets matching that rule, 100 at a time (API limit).

        Then, it gets even more complicated, because the first result batch does not include tweets
        made by our use (twitter_screen_name) as replies to his own root tweet.
        That's why we have to do a second request to get the tweets FROM out user, after the root tweet.
        We also accumulate up to 1000 tweets.

        The two results are merged together (up to 2000 tweets).

        Then we filter these tweets to search for those that are replies to our root tweet
        ('in_reply_to_status_id_str') == self.twitter_tweet_id.
        And we also keep tweets that are replies to replies to our root tweet (stay with me here).

        Needless to say this has to be modified as soon as Twitter provides some way to recover replies
        to a tweet. """

        self.ensure_one()

        search_query = {
            'to': self.twitter_screen_name,
            'since_id': self.twitter_tweet_id,
        }

        tweets_endpoint_url = url_join(self.env['social.media']._TWITTER_ENDPOINT, "/1.1/search/tweets.json")
        query_params = {
            'tweet_mode': 'extended',
            'result_type': 'recent',
            'count': 100,
            'include_entities': True,
        }
        answer_results = self._accumulate_tweets(tweets_endpoint_url, query_params, search_query)

        search_query = {
            'since_id': self.twitter_tweet_id,
            'from': self.twitter_screen_name
        }
        self_tweets = self._accumulate_tweets(tweets_endpoint_url, query_params, search_query)
        self_tweets = [tweet for tweet in self_tweets if tweet.get('id_str') not in [answer_tweet.get('id_str') for answer_tweet in answer_results]]

        all_tweets = list(answer_results) + list(self_tweets)
        sorted_tweets = sorted(all_tweets, key=lambda tweet: tweet.get('created_at'))

        filtered_tweets = []
        for tweet in sorted_tweets:
            if tweet.get('in_reply_to_status_id_str') == self.twitter_tweet_id:
                filtered_tweets.append(self.env['social.media']._format_tweet(tweet))
            else:
                for i in range(len(filtered_tweets)):
                    tested_against = [filtered_tweets[i].get('id')]
                    if filtered_tweets[i].get('comments'):
                        tested_against += [answer_tweet['id'] for answer_tweet in filtered_tweets[i]['comments']['data']]
                    if tweet.get('in_reply_to_status_id_str') in tested_against:
                        filtered_tweets[i]['comments'] = filtered_tweets[i].get('comments', {'data': []})
                        filtered_tweets[i]['comments']['data'] += [self.env['social.media']._format_tweet(tweet)]

        filtered_tweets = self._add_comments_favorites(filtered_tweets)

        return {
            'comments': list(reversed(filtered_tweets))
        }

    def _twitter_tweet_delete(self, tweet_id):
        self.ensure_one()
        delete_endpoint = url_join(self.env['social.media']._TWITTER_ENDPOINT, ('/1.1/statuses/destroy/%s.json' % tweet_id))
        headers = self.stream_id.account_id._get_twitter_oauth_header(
            delete_endpoint
        )
        requests.post(
            delete_endpoint,
            headers=headers,
            timeout=5
        )

        return True

    def _twitter_tweet_like(self, stream, tweet_id, like):
        favorites_endpoint = url_join(self.env['social.media']._TWITTER_ENDPOINT, (
            '/1.1/favorites/create.json' if like else '/1.1/favorites/destroy.json'
        ))
        headers = stream.account_id._get_twitter_oauth_header(
            favorites_endpoint,
            params={'id': tweet_id}
        )
        requests.post(
            favorites_endpoint,
            data={'id': tweet_id},
            headers=headers,
            timeout=5
        )

        return True

    # ========================================================
    # UTILITY / MISC
    # ========================================================

    def _add_comments_favorites(self, filtered_tweets):
        all_tweets_ids = []
        for tweet in filtered_tweets:
            all_tweets_ids.append(tweet.get('id'))
            if 'comments' in tweet:
                all_tweets_ids += [answer_tweet['id'] for answer_tweet in tweet['comments']['data']]

        favorites_by_id = self.stream_id._lookup_tweets(all_tweets_ids)

        for i in range(len(filtered_tweets)):
            looked_up_tweet = favorites_by_id.get(filtered_tweets[i]['id'], {'favorited': False})
            filtered_tweets[i]['user_likes'] = looked_up_tweet['favorited']

            if 'comments' in filtered_tweets[i]:
                for j in range(len(filtered_tweets[i]['comments']['data'])):
                    looked_up_tweet = favorites_by_id.get(filtered_tweets[i]['comments']['data'][j]['id'], {'favorited': False})
                    filtered_tweets[i]['comments']['data'][j]['user_likes'] = looked_up_tweet['favorited']

        return filtered_tweets

    def _accumulate_tweets(self, endpoint_url, query_params, search_query, query_count=1, force_max_id=None):
        self.ensure_one()

        copied_search_query = dict(search_query)
        if force_max_id:
            copied_search_query['max_id'] = force_max_id

        if 'max_id' in copied_search_query and int(copied_search_query['max_id']) < int(copied_search_query['since_id']):
            del copied_search_query['max_id']

        twitter_query_string = ''
        for key, value in copied_search_query.items():
            twitter_query_string += '%s:%s ' % (key, value)

        query_params['q'] = twitter_query_string

        headers = self.stream_id.account_id._get_twitter_oauth_header(
            endpoint_url,
            params=query_params,
            method='GET'
        )
        result = requests.get(
            endpoint_url,
            params=query_params,
            headers=headers,
            timeout=5
        )
        tweets = result.json().get('statuses')
        if query_count >= 10:
            return tweets
        elif not tweets:
            return []
        elif len(tweets) < 100:
            return tweets
        else:
            max_id = int(tweets[-1].get('id_str')) - 1
            if max_id < int(search_query['since_id']):
                return tweets
            return tweets + self._accumulate_tweets(
                endpoint_url,
                query_params,
                search_query,
                query_count=(query_count + 1),
                force_max_id=str(max_id)
            )
