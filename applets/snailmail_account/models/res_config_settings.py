# -*- coding: utf-8 -*-	
# For full licensing and copyright information, see the LICENSE file - Tele, INC.	

from tele import fields, models	


class ResConfigSettings(models.TransientModel):	
    _inherit = 'res.config.settings'	

    invoice_is_snailmail = fields.Boolean(string='Send by Post', related='company_id.invoice_is_snailmail', readonly=False)
