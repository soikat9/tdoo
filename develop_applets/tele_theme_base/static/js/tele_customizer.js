tele.define('tele_theme_setting.customizer', function (require) {
    "use strict";

    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');

    var TeleCustomizer = Widget.extend({
        template: 'tele_theme_base.customizer',
        sequence: 0,

        events: _.extend({}, Widget.prototype.events, {
            "click .customizer-toggle": "_on_toggle_click",
        }),

        _on_toggle_click: function (ev) {
            this.do_action({
                'type': 'ir.actions.act_url',
                'target': 'self'
            })
        }
    });

    SystrayMenu.Items.push(TeleCustomizer);

    return TeleCustomizer;
});
