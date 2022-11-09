# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import http, _
from tele.http import request


class TermsController(http.Controller):

    @http.route('/sign/terms', type='http', auth='public', website=True, sitemap=True)
    def terms_conditions(self, **kwargs):
        use_sign_terms = request.env['ir.config_parameter'].sudo().get_param('sign.use_sign_terms')
        if not (use_sign_terms and request.env.company.sign_terms_type == 'html'):
            return request.render('http_routing.http_error', {
                'status_code': _('Oops'),
                'status_message': _("""The requested page is invalid, or doesn't exist anymore.""")})
        values = {
            'use_sign_terms': use_sign_terms,
            'company': request.env.company
        }
        return request.render("sign.sign_terms_conditions_page", values)
