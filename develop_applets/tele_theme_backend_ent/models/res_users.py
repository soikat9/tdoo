# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from tele import models, fields, api

class User(models.Model):
    _inherit = "res.users"

    app_ids = fields.One2many('favorite.apps', 'user_id',string="Favorite Apps")
    bookmark_ids = fields.One2many('bookmark.link', 'user_id',string="Bookmark Links")
    dark_mode = fields.Boolean(string="Is dark Mode Active", default=False)
    vertical_sidebar_pinned = fields.Boolean(string="Pinned Sidebar", default=True)
    backend_theme_config = fields.Many2one('backend.config', string="Backend Config", copy=False)