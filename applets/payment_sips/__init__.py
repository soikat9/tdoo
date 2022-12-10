# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import models
from . import controllers

from tele.applets.payment import reset_payment_acquirer


def uninstall_hook(cr, registry):
    reset_payment_acquirer(cr, registry, 'sips')
