tele.define('tele_backend_theme_ent.settings', function(require) {
    "use strict";

    var BaseSettingRenderer = require('base.settings');
    var session = require('web.session');
    var __themesDB = require('tele_backend_theme_ent.TeleWebThemes');
    BaseSettingRenderer.Renderer.include({
        init: function() {
            this._super.apply(this, arguments);
            this.meniIcon = true;
        },
        willStart: function() {
            return Promise.all([this._getMenuIconType(), this._super.apply(this, arguments)]);
        },
        _getMenuIconType: function() {
            var themeData = __themesDB.get_theme_config_by_uid(session.uid);
            this.meniIcon = themeData.base_menu_icon;
        },
        start: function() {
            var self = this;
            self.$el.parents('.o_content').addClass('oe_base_settings');
            this._super.apply(this, arguments);
        },
        fileExists: function(filename) {
            filename = filename.trim();
            var response = jQuery.ajax({
                url: filename,
                type: 'HEAD',
                async: false
            }).status;
            return (response == "200");
        },
        /**
         * @override
         */
        on_attach_callback: function () {
            // set default focus on searchInput
            // this._super.apply(this, arguments);
            if (this.searchInput) {
                this.searchInput.focus();
            }
        },
        _getAppIconUrl: function(module) {
            var path;
            var custom_icon_path = '';
            if (this.meniIcon === 'base_icon') {
                custom_icon_path = "/base/static/description/";
                path = "/" + module + "/static/description/icon.png";
            } else if (this.meniIcon === '2d_icon') {
                custom_icon_path = '/tele_backend_theme_ent/static/src/img/menu_2d/';
                if (this.fileExists(custom_icon_path + module + '.png')) {
                    path = custom_icon_path + module + ".png"
                } else {
                    path = custom_icon_path + "/custom.png";
                    if (this.fileExists("/" + module + "/static/description/icon.png")) {
                        path = "/" + module + "/static/description/icon.png";
                    }
                }
            } else if (this.meniIcon === '3d_icon') {
                custom_icon_path = '/tele_backend_theme_ent/static/src/img/menu/';
                if (this.fileExists(custom_icon_path + module + '.png')) {
                    path = custom_icon_path + module + ".png"
                } else {
                    path = custom_icon_path + "/custom.png";
                    if (this.fileExists("/" + module + "/static/description/icon.png")) {
                        path = "/" + module + "/static/description/icon.png";
                    }
                }
            }
            return module === "general_settings" ? custom_icon_path + "/settings.png" : path;
        },
    });
});