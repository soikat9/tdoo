# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import http
from tele.http import request
from werkzeug.exceptions import Forbidden


class SocialValidationException(Exception):
    pass


class SocialController(http.Controller):

    def _get_social_stream_post(self, stream_post_id, media_type):
        """ Small utility method that fetches the post and checks it belongs
        to the correct media_type """
        stream_post = request.env['social.stream.post'].browse(int(stream_post_id))
        if not stream_post.exists() or stream_post.account_id.media_type != media_type:
            raise Forbidden()

        return stream_post
