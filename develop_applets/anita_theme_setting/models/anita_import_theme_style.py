# -*- coding: utf-8 -*-

from tele import models, fields


class AnitaImportThemeStyle(models.TransientModel):
    '''
    user theme style setting
    '''
    _name = 'anita_theme_setting.import_theme_style'
    _description = 'user setting'

    file = fields.Binary(string="Theme File", required=True)
