tele.define('tele_theme_backend_ent.ColorPalletJS', function (require) {
    'use strict';
    var Widget = require('web.Widget')
    var ColorPallet = Widget.extend({
        init: function (parent) {
            this._super(parent);
        },
        pallet_1: function() {
            $(':root').css({
                "--light-theme-primary-color": "#88B0CE",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#88B0CEb3',
            });
        },
        pallet_2: function() {
            $(':root').css({
                "--light-theme-primary-color": "#498264",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#498264b3',
            });
        },
        pallet_3: function() {
            $(':root').css({
                "--light-theme-primary-color": "#D393A3",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#D393A3b3',
            });
        },
        pallet_4: function() {
            $(':root').css({
                "--light-theme-primary-color": "#A495AF",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#A495AFb3',
            });
        },
        pallet_5: function() {
            $(':root').css({
                "--light-theme-primary-color": "#eb5858",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#eb5858b3',
            });
        },
        pallet_6: function() {
            $(':root').css({
                "--light-theme-primary-color": "#A69070",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#A69070b3',
            });
        },
        pallet_7: function() {
            $(':root').css({
                "--light-theme-primary-color": "#007a5a",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#007a5ab3',
            });
        },
        pallet_8: function() {
            $(':root').css({
                "--light-theme-primary-color": "#C2C1BF",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#C2C1BFb3',
            });
        },
        pallet_9: function() {
            $(':root').css({
                "--light-theme-primary-color": "#468296",
                "--light-theme-primary-text-color": "#ffffff",
                "--primary-rgba": '#468296b3',
            });
        },
        custom_color_pallet: function(record_dict) {
            $(':root').css({
                "--light-theme-primary-color": record_dict.light_primary_bg_color,
                "--light-theme-primary-text-color": record_dict.light_primary_text_color,
                "--primary-rgba": record_dict.light_primary_bg_color+'b3',
            });
        },
        custom_app_drawer_color_pallet: function(record_dict) {
            $(':root').css({
                "--app-drawer-custom-bg-color": record_dict.appdrawer_custom_bg_color,
                "--app-drawer-custom-text-color": record_dict.appdrawer_custom_text_color,
            });
        },
    });
    return ColorPallet
});