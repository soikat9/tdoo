# -*- coding: utf-8 -*-
# Part of Tele. See LICENSE file for full copyright and licensing details.

from datetime import timedelta
import random
import requests
import time

from tele import _, api, fields, models
from tele.exceptions import UserError

TIMEOUT = 20


class AddIomtBox(models.TransientModel):
    _name = 'add.iomt.box'
    _description = 'Add IoMT Box wizard'

    def _default_token(self):
        web_base_url = self.env['ir.config_parameter'].search([('key', '=', 'web.base.url')], limit=1)
        token = str(random.randint(1000000000, 9999999999))
        iomt_token = self.env['ir.config_parameter'].search([('key', '=', 'iomt_token')], limit=1)
        if iomt_token:
            # token valable 60 minutes
            if iomt_token.write_date + timedelta(minutes=60) > fields.datetime.now():
                token = iomt_token.value
            else:
                iomt_token.write({'value': token})
        else:
            self.env['ir.config_parameter'].create({'key': 'iomt_token', 'value': token})
        db_uuid = self.env['ir.config_parameter'].search([('key', '=', 'database.uuid')], limit=1).value or ''
        enterprise_code = self.env['ir.config_parameter'].search([('key', '=', 'database.enterprise_code')], limit=1).value or ''
        return web_base_url.value + '|' + token + '|' + db_uuid + '|' + enterprise_code

    token = fields.Char(string='Token', default=_default_token, store=False)
    pairing_code = fields.Char(string='Pairing Code')

    def box_pairing(self):
        data = {
            'params': {
                'pairing_code': self.pairing_code,
                'db_uuid': self.env['ir.config_parameter'].sudo().get_param('database.uuid'),
                'database_url': self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
                'enterprise_code': self.env['ir.config_parameter'].sudo().get_param('database.enterprise_code'),
                'token': self.env['ir.config_parameter'].sudo().get_param('iomt_token'),
            },
        }
        try:
            req = requests.post('https://iomt-proxy.tele.studio/tele-enterprise/iomt/connect-db', json=data, timeout=TIMEOUT)
        except requests.exceptions.ReadTimeout:
            raise UserError(_("We had troubles pairing your IoMT Box. Please try again later."))

        response = req.json()

        if 'error' in response:
            if response['error']['code'] == 404:
                raise UserError(_("The pairing code you provided was not found in our system. Please check that you entered it correctly."))
            else:
                raise requests.exceptions.ConnectionError()
        else:
            time.sleep(12)  # The IoMT Box only polls the server every 10 seconds
            return self.reload_page()

    def reload_page(self):
        return self.env["ir.actions.actions"]._for_xml_id("iomt.iomt_box_action")