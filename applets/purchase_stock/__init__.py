# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from . import report
from . import populate
from . import wizard

from tele import api, SUPERUSER_ID


def _create_buy_rules(cr, registry):
    """ This hook is used to add a default buy_pull_id on every warehouse. It is
    necessary if the purchase_stock module is installed after some warehouses
    were already created.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    warehouse_ids = env['stock.warehouse'].search([('buy_pull_id', '=', False)])
    warehouse_ids.write({'buy_to_resupply': True})
