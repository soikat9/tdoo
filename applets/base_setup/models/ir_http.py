# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.
from tele import models
from tele.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        if request.env.user.has_group('base.group_user'):
            result['show_effect'] = request.env['ir.config_parameter'].sudo().get_param('base_setup.show_effect')
        return result
