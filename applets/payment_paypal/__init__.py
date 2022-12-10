# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from . import controllers
from . import models

from tele.applets.payment import reset_payment_acquirer


def uninstall_hook(cr, registry):
    reset_payment_acquirer(cr, registry, 'paypal')
