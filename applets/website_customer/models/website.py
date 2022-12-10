# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, _
from tele.applets.http_routing.models.ir_http import url_for


class Website(models.Model):
    _inherit = "website"

    def get_suggested_controllers(self):
        suggested_controllers = super(Website, self).get_suggested_controllers()
        suggested_controllers.append((_('References'), url_for('/customers'), 'website_customer'))
        return suggested_controllers
