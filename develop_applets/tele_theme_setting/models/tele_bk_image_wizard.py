# -*- coding: utf-8 -*-

from tele import models, fields, api


class TeleBkImageWizard(models.TransientModel):
    '''
    Model Project
    '''
    _name = 'tele_theme_setting.background_image_wizard'
    _description = 'background image wizard'

    data = fields.Binary(string='data', required=True)
    opacity = fields.Float(string='theme opacity', default=0.8)
