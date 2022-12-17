# -*- coding: utf-8 -*-
# Part of Tele. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from . import models

from tele import api, SUPERUSER_ID, _
from os.path import isfile
from tele.modules import get_module_resource


def post_init_check(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    modules = env['ir.module.module'].search([])
    menu_ids = env['ir.ui.menu'].get_user_roots().mapped('id')
    board_id = env.ref('base.menu_board_root').id
    menu_ids.append(board_id)
    menus = env['ir.ui.menu'].browse(menu_ids)
    for module in modules:
        path_info = module.icon
        module.write({'theme_icon': path_info})

    for menu in menus:
        if menu.web_icon:
            path_info = menu.web_icon
            menu.write({'theme_icon': path_info})
            env['ir.ui.menu'].icon_menu_chnange({'base_menu_icon': '3d_icon'})


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    custom_url = env['web_editor.assets'].make_custom_asset_file_url('/tele_backend_theme_ent/static/src/scss/variables.scss', 'web.assets_backend')
    custom_attachment = env['web_editor.assets']._get_custom_attachment(custom_url)
    custom_assets = env['ir.asset'].search([])
    if custom_assets:
        custom_assets.unlink()
    custom_attachment.unlink()
        