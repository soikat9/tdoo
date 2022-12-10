# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models
from tele.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _get_translation_frontend_modules_name(cls):
        mods = super(IrHttp, cls)._get_translation_frontend_modules_name()
        return mods + ['portal']

    @classmethod
    def _get_frontend_langs(cls):
        if request and request.is_frontend:
            return [lang[0] for lang in filter(lambda l: l[3], request.env['res.lang'].get_available())]
        return super()._get_frontend_langs()
