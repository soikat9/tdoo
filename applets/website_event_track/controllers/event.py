# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele.applets.website_event.controllers.main import WebsiteEventController


class EventOnlineController(WebsiteEventController):

    def _get_registration_confirm_values(self, event, attendees_sudo):
        values = super(EventOnlineController, self)._get_registration_confirm_values(event, attendees_sudo)
        values['hide_sponsors'] = True
        return values
