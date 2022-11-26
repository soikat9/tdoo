# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    expense_extract_show_ocr_option_selection = fields.Selection([
        ('no_send', 'Do not digitalize'),
        ('manual_send', "Digitalize on demand only"),
        ('auto_send', 'Digitalize automatically')], string="Send mode on expense attachments",
        required=False, default='auto_send')
