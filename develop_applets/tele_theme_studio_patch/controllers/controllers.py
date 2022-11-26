# -*- coding: utf-8 -*-
 from tele import http


class TeleThemeStudioPatch(http.Controller):
    @http.route('/tele_theme_studio_patch/tele_theme_studio_patch', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/tele_theme_studio_patch/tele_theme_studio_patch/objects', auth='public')
    def list(self, **kw):
        return http.request.render('tele_theme_studio_patch.listing', {
            'root': '/tele_theme_studio_patch/tele_theme_studio_patch',
            'objects': http.request.env['tele_theme_studio_patch.tele_theme_studio_patch'].search([]),
        })

    @http.route('/tele_theme_studio_patch/tele_theme_studio_patch/objects/<model("tele_theme_studio_patch.tele_theme_studio_patch"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('tele_theme_studio_patch.object', {
            'object': obj
        })
