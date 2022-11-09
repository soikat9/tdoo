# -*- encoding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class IotTrigger(models.Model):
    _inherit = 'iot.trigger'

    action = fields.Selection(selection_add=[('pass', 'Pass'),
                               ('fail', 'Fail'),
                               ('measure', 'Take Measure')])
