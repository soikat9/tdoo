tele.define('tele_backend_theme_ent.WebThemesDB', function(require) {
    "use strict";

    var core = require('web.core');
    /* The WebThemesDB holds reference to data */

    var WebThemesDB = core.Class.extend({
        name: 'tele_web_themes_db', //the prefix of the localstorage data
        limit: 100, // the maximum number of results returned by a search
        init: function(options) {
            options = options || {};
            this.name = options.name || this.name;
            this.limit = options.limit || this.limit;
            this.web_themes = [];
            this.users_config = [];
            this.theme_by_id = {};
            this.theme_config_by_uid = {};
            this.default_web_theme = {};
        },

        add_themes: function(themes_data) {
            var self = this;
            this.web_themes = themes_data.themes;
            this.users_config = themes_data.users_config;
            this.default_web_theme = _.findWhere(this.web_themes, { selected: true });
            for (var i = 0, len = this.web_themes.length; i < len; i++) {
                var theme = this.web_themes[i];
                self.theme_by_id[theme.id] = theme;
            };

            for (var i = 0, len = this.users_config.length; i < len; i++) {
                var uConfig = self.users_config[i];
                self.theme_config_by_uid[uConfig.id] = uConfig;
            };

        },

        get_themes: function() {
            return this.web_themes;
        },

        get_theme_by_id: function(id) {
            return this.theme_by_id[id];
        },

        get_theme_config_by_uid: function(uid) {
            // Remove uid to merge with theme properties
            var configs = _.omit(this.theme_config_by_uid[uid], 'id');
            var fieldsToIgnore = _.keys(configs);
            // Remove user config fields
            var themeProperties = _.omit(this.default_web_theme, function(v, k, o) {
                return _.contains(fieldsToIgnore, k);
            });
            // Merge user configs and theme properties
            return _.extend(configs, themeProperties);
        },

        getUserThemeConfigs: function() {
            return this.users_config;
        },
    });

    return WebThemesDB;

});