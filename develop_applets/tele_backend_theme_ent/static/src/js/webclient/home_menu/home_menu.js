/** @tele-module **/

import { HomeMenu } from "@web_enterprise/webclient/home_menu/home_menu";
import { useService } from "@web/core/utils/hooks";
import { sprintf } from "@web/core/utils/strings";
const { Component, hooks } = owl;
const { useExternalListener, useState, useRef } = hooks;
import { patch } from 'web.utils';
const session = require('web.session');
var core = require('web.core');

patch(HomeMenu.prototype, '@tele_backend_theme_ent/webclient/navbar/navbar.js', {
    setup() {
        this._super();
        this.notification = useService("notification");
        this.companyService = useService("company");
        this.state.favoriteMenuById = {};
        this.state.menuEdit = false;
    },
    async _getFavMenuData() {
        self = this
        var favorites = await this.env.services.orm.call("ir.favorite.menu", "get_favorite_menus")
        if (favorites) {
            favorites.forEach(function(menu) {
                self.state.favoriteMenuById[menu.favorite_menu_id[0]] = menu.id;
            });
        }
    },
    async _onClickFavorite(payload) {
        var self = this;
        if (_.has(this.state.favoriteMenuById, payload.id)) {
            var favoriteMenuId = this.state.favoriteMenuById[payload.id]
            self.bindToRemoveOnUnFavorited(payload, favoriteMenuId);
        } else {
            self._makeFavorited(payload.label, {
                favorite_menu_id: payload.id,
                favorite_menu_xml_id: payload.xmlid,
                favorite_menu_action_id: payload.actionID,
                user_id: session.uid
            });
        }
    },
    async _makeFavorited(name, values) {
        const value = await this.env.services.orm.call("ir.favorite.menu", "create", [values]);
        this.state.favoriteMenuById[values.favorite_menu_id] = value;
        core.bus.trigger('click_favorite_menu');
        const message = sprintf(this.env._t('%s added to favorite.'), name);
        this.notification.add(message, { type: "success" }, );
    },
    async bindToRemoveOnUnFavorited(values, favoriteMenuId) {
        const value = await this.env.services.orm.call("ir.favorite.menu", "unlink", [favoriteMenuId]);
        delete this.state.favoriteMenuById[values.appID]
        core.bus.trigger('click_favorite_menu');
        const message = sprintf(this.env._t('%s removed to favorite.'), values.label);
        this.notification.add(message, { type: "danger" });
    },
    getCurrentCompany() {
        const company = this.companyService.currentCompany;
        if (company && company.id) {
            const url = '/web/image/res.company/' + company.id + '/logo/180x55';
            return url;
        }
        return false;
    },
    _onAppClick(app) {
        if (this.state.menuEdit) { return; }
        this._super(...arguments);
    },
    onEditMenu(ev) {
        var inputval = this.inputRef.el.value;
        if (inputval) {
            this.inputRef.el.value = '';
            this.state.query = '';
            this.availableApps = this.props.apps;
            this.displayedMenuItems = [];
        };
        this.state.menuEdit = !this.state.menuEdit;
        const $searchmenu = $('.o_menu_search');
        $searchmenu.toggleClass('invisible', !!this.state.menuEdit);
        Promise.all([this._getFavMenuData()])
    },
});