# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.http import request
from tele.applets.website_helpdesk.controllers import main


class WebsiteHelpdesk(main.WebsiteHelpdesk):

    def get_helpdesk_team_data(self, team, search=None):
        result = super(WebsiteHelpdesk, self).get_helpdesk_team_data(team, search)
        result['channel'] = team.elearning_id
        domain = []
        if search:
            domain += [('name', 'ilike', search)]
        if team.elearning_id:
            domain += [('channel_id', '=', result['channel'].id)]
            slides = request.env['slide.slide'].search(domain)
            result['slides'] = slides[:7]
            result['slides_limit'] = len(slides)
            result['search'] = search
        return result
