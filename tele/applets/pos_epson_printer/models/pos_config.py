# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    epson_printer_ip = fields.Char(string='Epson Printer IP', help="Local IP address of an Epson receipt printer.")

    @api.onchange('epson_printer_ip')
    def _onchange_epson_printer_ip(self):
        if self.epson_printer_ip in (False, ''):
            self.iface_cashdrawer = False
