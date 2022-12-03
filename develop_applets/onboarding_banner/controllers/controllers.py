# -*- coding: utf-8 -*-

from tele import http


class OnboardingBanner(http.Controller):
    @http.route('/onboarding_banner/onboarding_banner', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/onboarding_banner/onboarding_banner/objects', auth='public')
    def list(self, **kw):
        return http.request.render('onboarding_banner.listing', {
            'root': '/onboarding_banner/onboarding_banner',
            'objects': http.request.env['onboarding_banner.onboarding_banner'].search([]),
        })

    @http.route('/onboarding_banner/onboarding_banner/objects/<model("onboarding_banner.onboarding_banner"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('onboarding_banner.object', {
            'object': obj
        })
