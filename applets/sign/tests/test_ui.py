# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import tele.tests

from .test_common import TestSignCommon
from tele.tools.misc import mute_logger
from tele.tools.translate import WEB_TRANSLATION_COMMENT


@tele.tests.tagged('-at_install', 'post_install')
class TestUi(tele.tests.HttpCase, TestSignCommon):
    def test_ui(self):
        self.start_tour("/web", 'sign_widgets_tour', login='admin')

    def test_translate_sign_instructions(self):
        self.env['res.lang'].create({
            'name': 'Parseltongue',
            'code': 'pa_GB',
            'iso_code': 'pa_GB',
            'url_code': 'pa_GB',
        })
        with mute_logger('tele.applets.base.models.ir_translation'):
            self.env["base.language.install"].create({'lang': 'pa_GB'}).lang_install()
        self.env['ir.translation'].create({
            'type': 'code',
            'name': 'applets/sign/static/src/js/sign_common.js',
            'lang': 'pa_GB',
            'module': 'sign',
            'src': "Click to start",
            'value': "Click to ssssssstart",
            'state': 'translated',
            'comments': WEB_TRANSLATION_COMMENT,
        })

        # Once `website` is installed, the available langs are only the ones
        # from the website, which by default is just the `en_US` lang.
        langs = self.env['res.lang'].with_context(active_test=False).search([]).get_sorted()
        self.patch(self.registry['res.lang'], 'get_available', lambda self: langs)
        self.partner_id.lang = "pa_GB"
        url = f"/sign/document/{self.single_role_sign_request.id}/{self.single_role_sign_request.request_item_ids.access_token}"
        self.start_tour(url, 'translate_sign_instructions', login=None)
