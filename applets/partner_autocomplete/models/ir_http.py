# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models
from tele.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        """ Add information about iap enrich to perform """
        session_info = super(Http, self).session_info()
        if session_info.get('is_admin'):
            session_info['iap_company_enrich'] = not request.env.user.company_id.iap_enrich_auto_done
        return session_info
