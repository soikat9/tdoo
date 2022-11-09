# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

# Updating mako environement in order to be able to use slug
try:
    from tele.tools.rendering_tools import template_env_globals
    from tele.applets.http_routing.models.ir_http import slug

    template_env_globals.update({
        'slug': slug
    })
except ImportError:
    pass

from . import controllers
from . import models
from . import wizard
