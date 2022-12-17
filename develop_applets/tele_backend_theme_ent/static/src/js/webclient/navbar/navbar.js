/** @tele-module **/

import { EnterpriseNavBar } from "@web_enterprise/webclient/navbar/navbar";
import { useService } from "@web/core/utils/hooks";
const { hooks, useState } = owl;
const core = require('web.core');
const config = require('web.config');
const { useExternalListener } = hooks;
import { patch } from 'web.utils';
import { browser } from "@web/core/browser/browser";

patch(EnterpriseNavBar.prototype, '@tele_backend_theme_ent/webclient/navbar/navbar.js', {
    setup() {
        this._super();
        this.menuService = useService("menu");
        this.debug = config.isDebug() ? '?debug' : '';
        this.isTouchDevice = config.device.touch;
        this.user = useService("user");
        this.state = useState({
            favoriteMenuNameById: {},
            menus: [],
        });
        core.bus.on('click_favorite_menu', this, this._getFavMenuData);
        useExternalListener(window, "click", this._getfullScreen);
    },
    async willStart() {
        const prom = await this._super.apply(this, arguments);
        await this._getFavMenuData();
        return prom;
    },
    _getfullScreen(ev) {
        if (this.isTouchDevice && !this.el.contains(ev.target) &&
            !document.body.classList.contains('ad_full_view')) {
            $('body').toggleClass('ad_full_view');
        }
    },
    async _getFavMenuData() {
        var self = this;
        var favorites = await this.env.services.orm.call("ir.favorite.menu", "get_favorite_menus");
        if (favorites) {
            favorites.forEach(function(menu) {
                self.state.favoriteMenuNameById[menu.favorite_menu_id[0]] = menu.favorite_menu_id[1];
            });
            self.state.menus = favorites.map(function(menu) {
                return _.extend(menu, {
                    theme_icon_data: menu.theme_icon_data && ('data:image/png;base64,' + menu.theme_icon_data).replace(/\s/g, "") || menu.web_icon_data && ('data:image/png;base64,' + menu.web_icon_data).replace(/\s/g, "") || false,
                    actionID: menu.favorite_menu_action_id,
                    xmlid: menu.favorite_menu_xml_id,
                    parents: "",
                    appID: menu.favorite_menu_id[0],
                    action() {
                        $('.o_menu_systray').removeClass('show');
                        self.menuService.selectMenu(menu);
                    },
                });
            });
        }
    },
    async render() {
        await this._super.apply(this, arguments);
        var self = this;
        const favorite_menu = this.el && this.el.querySelector('.oe_apps_menu');
        if (favorite_menu) {
            $(favorite_menu).sortable({
                items: "> .oe_favorite",
                axis: 'y',
                stop: (event, ui) => {
                    $(favorite_menu).children().each(function(index) {
                        var vals = {};
                        var menu_id = $(this).data('id');
                        vals['sequence'] = index;
                        vals['favorite_menu_id'] = $(this).data('menu-id');
                        self.env.services.orm.call("ir.favorite.menu", "write", [
                            [menu_id], vals
                        ]);
                    });
                },
            });
        }
    },
    get userData() {
        const { origin } = browser.location;
        const { userId } = this.user;
        this.source = `${origin}/web/image?model=res.users&field=avatar_128&id=${userId}`;
        return this.source;
    },
    onOpenMenu() {
        return this.state.menus;
    },
    OpenMenu(menu) {
        this.menuService.setCurrentMenu(menu.appID);
        menu.action();
    },
    onFullViewClicked() {
        $('body').toggleClass('ad_full_view');
    },
    onFullScreen() {
        document.fullScreenElement && null !== document.fullScreenElement || !document.mozFullScreen &&
            !document.webkitIsFullScreen ? document.documentElement.requestFullScreen ? document.documentElement.requestFullScreen() :
            document.documentElement.mozRequestFullScreen ? document.documentElement.mozRequestFullScreen() :
            document.documentElement.webkitRequestFullScreen && document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT) :
            document.cancelFullScreen ? document.cancelFullScreen() :
            document.mozCancelFullScreen ? document.mozCancelFullScreen() :
            document.webkitCancelFullScreen && document.webkitCancelFullScreen()
    },
    CloseUserMenu() {
        $('.o_menu_systray').removeClass('show');
    },
    _updateMenuAppsIcon() {
        this._super(...arguments);
        const menuAppsEl = this.menuAppsRef.el;
        menuAppsEl.classList.remove('fa-th', 'fa-chevron-left');
        menuAppsEl.classList.toggle("__has_action", !this.isInApp && this.hasBackgroundAction);
    },
});