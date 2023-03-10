# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import logging
import tele.tests

_logger = logging.getLogger(__name__)


@tele.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(tele.tests.HttpCase):

    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "tele.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "tele.isReady === true", login="admin", timeout=600)
                self.terminate_browser()


@tele.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(tele.tests.HttpCase):

    def test_01_click_everywhere_as_demo(self):
        user_demo = self.env.ref("base.user_demo")
        menus = self.env['ir.ui.menu'].with_user(user_demo.id).load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "tele.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "tele.isReady === true", login="demo", timeout=600)
                self.terminate_browser()

@tele.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(tele.tests.HttpCase):

    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "tele.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "tele.isReady === true", login="admin", timeout=120)

@tele.tests.tagged('post_install', '-at_install',)
class TestMenusDemoLight(tele.tests.HttpCase):

    def test_01_click_apps_menus_as_demo(self):
        self.browser_js("/web", "tele.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "tele.isReady === true", login="demo", timeout=120)
