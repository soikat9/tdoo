# -*- coding: utf-8 -*-

from tele import models, fields, api, exceptions
import json
import re
from tele.tools.config import config

try:
    import sass as libsass
except ImportError:
    libsass = None


class TeleThemeMode(models.Model):
    '''
    user theme style setting
    '''
    _inherit = 'tele_theme_setting.theme_mode'
    _description = 'tele theme mode'

    def _compile_scss(self):
        """
        This code will compile valid scss into css.
        Simply copied and adapted slightly
        """
        if debug := config.get('debug', False):
            # tele get resource path
            from tele.modules.module import get_resource_path
            tmp_path = get_resource_path(
                'tele_theme_enterprise', 'static', 'template', 'template1.scss')
            # read the file content
            with open(tmp_path, 'r') as f:
                template = f.read()
        else:
            template = self.mode_template.template

        scss_source = template.strip()
        mode_name = "body.{name}".format(name=self.name)
        scss_source = scss_source.replace('body.__mode_name__', mode_name)
        scss_source = scss_source.replace(
            'body.$mode_name', "body.{name}".format(name=self.name))
        if not scss_source:
            return ""

        template_vars = json.loads(self.template_vars or "{}")
        for name, value in template_vars.items():
            scss_source = scss_source.replace(name, value)

        precision = 8
        output_style = 'expanded'

        from tele.modules.module import get_resource_path

        bootstrap_scss_path = get_resource_path('web', 'static', 'lib', 'bootstrap', 'scss')
        tele_mixins = get_resource_path('tele_theme_base', 'static', 'css')

        try:
            result = libsass.compile(
                string=scss_source,
                include_paths=[bootstrap_scss_path, tele_mixins],
                output_style=output_style,
                precision=precision)
            index = result.find(mode_name)
            result = result[index:]
            return result
        except libsass.CompileError as e:
            raise libsass.CompileError(e.args[0]) from e