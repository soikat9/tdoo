# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        if self.env.user.has_group('base.group_user'):
            res['max_time_between_keys_in_ms'] = int(
                self.env['ir.config_parameter'].sudo().get_param('barcode.max_time_between_keys_in_ms', default='100'))
        return res
