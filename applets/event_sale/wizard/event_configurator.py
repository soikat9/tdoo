# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields


class EventConfigurator(models.TransientModel):
    _name = 'event.event.configurator'
    _description = 'Event Configurator'

    product_id = fields.Many2one('product.product', string="Product", readonly=True)
    event_id = fields.Many2one('event.event', string="Event")
    event_ticket_id = fields.Many2one('event.event.ticket', string="Event Ticket")
