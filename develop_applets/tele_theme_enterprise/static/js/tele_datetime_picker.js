tele.define('tele_theme_enterprise.datepicker', function (require) {
    "use strict";
    
    var DatePicker = require("web.datepicker").DateWidget

    DatePicker.include({

        _onDateTimePickerShow: function () {
            this._super.apply(this, arguments);
            this.$('.o_datepicker_button').addClass('tele_reverse')
        },

        _onDateTimePickerHide: function () {
            this._super.apply(this, arguments);
            this.$('.o_datepicker_button').removeClass('tele_reverse')
        },
    })
})