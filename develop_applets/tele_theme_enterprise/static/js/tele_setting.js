tele.define('tele_theme_enterprise.settings', function (require) {
    "use strict";

    var settings = require('base.settings')
    var BaseSettingRenderer = settings.Renderer

    var BaseSettingRenderer = BaseSettingRenderer.include({

        events: _.extend({}, BaseSettingRenderer.prototype.events, {
            "click .tele_setting_toggler": "_on_toggler_click"
        }),

        _on_toggler_click: function (event) {
            if (this.$('.settings_tab').hasClass('show')) {
                this.$('.settings_tab').removeClass('show')
                this.$('.tele_setting_toggler .left_arrow').addClass('d-none')
                this.$('.tele_setting_toggler .right_arrow').removeClass('d-none')
            } else {
                this.$('.settings_tab').addClass('show')
                this.$('.tele_setting_toggler .left_arrow').removeClass('d-none')
                this.$('.tele_setting_toggler .right_arrow').addClass('d-none')
            }
        }
    });
});
