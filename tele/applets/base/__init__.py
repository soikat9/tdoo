# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import controllers
from . import models
from . import populate
from . import report
from . import wizard


def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from tele import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].init(force=True)
