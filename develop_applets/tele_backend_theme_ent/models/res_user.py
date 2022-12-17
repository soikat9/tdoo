# -*- coding: utf-8 -*-
# Part of Tele. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from tele import fields, models, api, modules
from tele.modules import get_module_resource


class ResUsers(models.Model):
    _inherit = 'res.users'

    display_density = fields.Selection([
                ('default', 'Default'),
                ('comfortable', 'Comfortable'),
                ('compact', 'Compact'),
            ], string="Display Density", default='default')
    tab_type = fields.Selection([
                ('horizontal_tabs', 'Horizontal Tabs'),
                ('vertical_tabs', 'Vertical Tabs'),
            ], string="Tab Type", default='vertical_tabs')
    tab_configration = fields.Selection([
                ('open_tabs','Open Tabs'),
                ('close_tabs','Close Tabs',),
            ], default='open_tabs')
    base_menu = fields.Selection([
                ('base_menu','Horizontal Menu'),
                ('theme_menu','Vertical Menu'),
            ], default='theme_menu')
    font_type_values = fields.Selection([
                ("inter",'Inter'),
                ("roboto",'Roboto'), 
                ("poppins",'Poppins'), 
                ("publicsans",'Public Sans'),
                ("raleway",'Raleway'),
                ("rubik",'Rubik'),        
            ], default='inter')
    chatter = fields.Selection([
        ('chatter_close', 'Close'),
        ('chatter_open', 'Open'),
        ], default='chatter_close')
    mode = fields.Selection([
        ('light_mode_on', 'Light Mode'),
        ('night_mode_on', 'Night Mode'),
        ('normal_mode_on', 'Normal Mode'),
        ], default='normal_mode_on')

    @api.model
    def get_users_themes(self):
        return self.search_read([('share', '=', False)], [
            'display_density', 'tab_type', 'tab_configration',
            'base_menu', 'font_type_values', 'mode', 'chatter'
        ])

    def get_module_theme_icon(self, module):
        icon = module + '.png'
        current_theme = self.env['ir.web.theme'].get_current_theme()
        theme_type = self.env['ir.web.theme'].browse(int(current_theme))
        if theme_type.base_menu_icon == '3d_icon':
            iconpath = ['static', 'src', 'img', 'menu', icon]
        elif theme_type.base_menu_icon == '2d_icon':
            iconpath = ['static', 'src', 'img', 'menu_2d', icon]
        else:
            return modules.module.get_module_icon(module)
        if modules.module.get_module_resource(module, *iconpath):
            return ('/' + 'tele_backend_theme_ent' + '/') + '/'.join(iconpath)
        return '/tele_backend_theme_ent/'  + '/'.join(iconpath)

    @api.model
    def systray_get_activities(self):
        res = super(ResUsers, self).systray_get_activities()
        for resList in res:
            module = self.env[resList['model']]._original_module
            icon = module and self.get_module_theme_icon(module)
            resList['icon'] = icon
        return res
