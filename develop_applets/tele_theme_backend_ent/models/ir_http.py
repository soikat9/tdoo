# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details

from tele import api, models
from tele.http import request

class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        # Show company change option even if single company available 
        res = super(Http, self).session_info()
        user = request.env.user

        if self.env.user.has_group('base.group_user'):
            res.update({
                "display_switch_company_menu": True,
            })
        return res