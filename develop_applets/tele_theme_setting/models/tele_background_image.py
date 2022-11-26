# -*- coding: utf-8 -*-

from tele import models, fields, api, exceptions
from tele.modules.module import get_resource_path
import base64
from .tele_utility import split_module_and_path


class TeleThemeSettingBackgroundImage(models.Model):
    '''
    Model Project
    '''
    _name = 'tele_theme_setting.background_image'
    _description = 'background image'

    data = fields.Image(string='data')
    opacity = fields.Float(string='theme opacity', default=0.8)

    def get_image_url(self):
        """
        get image url
        """
        return f'web/image/tele_theme_setting.background_image/{str(self.id)}/data'
