# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import tele.http as http

from tele.http import request, content_disposition


class Partner(http.Controller):

    @http.route('/web_enterprise/partner/<model("res.partner"):partner>/vcard', type='http', auth="user")
    def download_vcard(self, partner, **kwargs):
        content = partner._get_vcard_file()
        if not content:
            return request.not_found()
        return request.make_response(content, [
            ('Content-Type', 'text/vcard'),
            ('Content-Length', len(content)),
            ('Content-Disposition', content_disposition('%s.vcf' % partner.name))
        ])
