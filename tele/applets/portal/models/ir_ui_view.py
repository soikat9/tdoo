# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models, fields
from tele.http import request
from tele.applets.http_routing.models.ir_http import url_for
from tele.tools import is_html_empty


class View(models.Model):
    _inherit = "ir.ui.view"

    customize_show = fields.Boolean("Show As Optional Inherit", default=False)

    @api.model
    def _prepare_qcontext(self):
        """ Returns the qcontext : rendering context with portal specific value (required
            to render portal layout template)
        """
        qcontext = super(View, self)._prepare_qcontext()
        if request and getattr(request, 'is_frontend', False):
            Lang = request.env['res.lang']
            portal_lang_code = request.env['ir.http']._get_frontend_langs()
            qcontext.update(dict(
                self._context.copy(),
                languages=[lang for lang in Lang.get_available() if lang[0] in portal_lang_code],
                url_for=url_for,
                is_html_empty=is_html_empty,
            ))
        return qcontext