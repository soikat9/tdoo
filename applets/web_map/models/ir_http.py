# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        if self.env.user.has_group('base.group_user'):
            result.update(
                map_box_token = self.env['ir.config_parameter'].sudo().get_param('web_map.token_map_box',False)
            )
        return result
