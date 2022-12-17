tele.define('tele_backend_theme_ent.DialingPanel', function(require) {
    "use strict";

    const { device } = require("web.config");

    if ((!_.contains(tele._modules, 'voip') &&
            !_.has(tele.__DEBUG__.services, 'voip.DialingPanel')) || device.isMobile) { return; };

    const DialingPanel = require('voip.DialingPanel');

    DialingPanel.include({

        _removeChatWindowClass() {
            var $body = $('body');
            if ($body.hasClass('ad-chat-window') && !$('.o_ChatWindow').length) {
                $body.removeClass('ad-chat-window');
            };
        },

        _onClickWindowClose(ev) {
            this._removeChatWindowClass();
            return this._super.apply(this, arguments);
        },

        async _onToggleDisplay() {
            var _super = await this._super.apply(this, arguments);
            if (this._isShow) {
                $('body').addClass('ad-chat-window');
            } else {
                this._removeChatWindowClass();
            }
            return _super;
        },
    });

});