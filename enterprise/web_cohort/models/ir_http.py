# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    # TODO: remove in master and rephrase "Average" instead
    # make web_cohort "Average" available in frontend since it may override
    # portal_rating
    @classmethod
    def _get_translation_frontend_modules_name(cls):
        mods = super()._get_translation_frontend_modules_name()
        return mods + ['web_cohort']
