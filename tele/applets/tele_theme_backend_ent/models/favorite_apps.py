# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from tele import models, fields, api

class FavoriteApps(models.Model):
    _name = "favorite.apps"
    _description = "Favorite Apps"

    name = fields.Char("Name")
    app_id = fields.Char("App Id")
    app_xmlid = fields.Char("App XML Id")
    app_actionid = fields.Char("App Action Id")
    user_id = fields.Many2one('res.users')