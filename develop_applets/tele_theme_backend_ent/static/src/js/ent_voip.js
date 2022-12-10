tele.define('tele_theme_backend_ent.teleVoipJs', function (require) {
    'use strict';
    var DialingPanel = require('voip.DialingPanel')
    const HEIGHT_OPEN = '480px';
    const HEIGHT_FOLDED = '0px';
    DialingPanel.include({
        _fold(animate = true) {
            $('.o_dial_transfer_button').popover('hide');
            if (animate) {
                this.$el.animate({
                    height: this._isFolded ? HEIGHT_FOLDED : HEIGHT_OPEN,
                });
            } else {
                this.$el.height(this._isFolded ? HEIGHT_FOLDED : HEIGHT_OPEN);
            }
            if (this._isFolded) {
                this.$('.o_dial_fold').css("bottom", "38px");
                this.$('.o_dial_main_buttons').hide();
                this.$('.o_dial_incoming_buttons').hide();
            } else {
                this.$('.o_dial_fold').css("bottom", 0);
                this.$('.o_dial_main_buttons').show();
            }
        },
    })
});