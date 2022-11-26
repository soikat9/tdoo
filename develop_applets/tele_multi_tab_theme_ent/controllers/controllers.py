# -*- coding: utf-8 -*-
from tele import http


class TeleMultiTabThemeEnt(http.Controller):
    @http.route('/tele_multi_tab_theme_ent/tele_multi_tab_theme_ent', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tele_multi_tab_theme_ent/tele_multi_tab_theme_ent/objects', auth='public')
    def list(self, **kw):
        return http.request.render('tele_multi_tab_theme_ent.listing', {
            'root': '/tele_multi_tab_theme_ent/tele_multi_tab_theme_ent',
            'objects': http.request.env['tele_multi_tab_theme_ent.tele_multi_tab_theme_ent'].search([]),
        })

    @http.route('/tele_multi_tab_theme_ent/tele_multi_tab_theme_ent/objects/<model("tele_multi_tab_theme_ent.tele_multi_tab_theme_ent"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tele_multi_tab_theme_ent.object', {
            'object': obj
        })
