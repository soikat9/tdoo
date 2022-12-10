# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models
from tele.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super().session_info()
        if result['is_admin']:
            demo_modules_count = self.env['ir.module.module'].sudo().search_count([('demo', '=', True)])
            result['web_tours'] = request.env['web_tour.tour'].get_consumed_tours()
            result['tour_disable'] = demo_modules_count > 0
        return result
