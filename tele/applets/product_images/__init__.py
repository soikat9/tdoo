# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from . import wizard

from tele import api, SUPERUSER_ID


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    ICP = env['ir.config_parameter']
    ICP.set_param('google.custom_search.cx', False)
    ICP.set_param('google.custom_search.key', False)
