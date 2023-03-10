# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models, fields, _

class SaveSpreadsheetTemplate(models.TransientModel):
    _name = 'save.spreadsheet.template'
    _description= "Spreadsheet Template Save Wizard"

    template_name = fields.Char(required=True)
    data = fields.Binary()
    thumbnail = fields.Binary()

    def save_template(self):
        self.ensure_one()
        self.env['spreadsheet.template'].create({
            'name': self.template_name,
            'data': self.data,
            'thumbnail': self.thumbnail,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': _('"%s" saved as template', self.template_name),
                'sticky': False,
                'type': 'info',
            }
        }
