# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models

def post_init(cr, registry):
    from tele import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})

    fsm_product = env.ref("industry_fsm.field_service_product", raise_if_not_found=False)
    if fsm_product:
        fsm_product.write(
            {"worksheet_template_id": env.ref("industry_fsm_report.fsm_worksheet_template").id, }
        )
