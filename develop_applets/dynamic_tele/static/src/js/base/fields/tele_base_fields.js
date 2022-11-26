tele.define('dynamic_tele.tele_basic_fields', function (require) {
    "use strict";

    var AbstractField = require('web.AbstractField');

    AbstractField.include({
        init: function (parent, name, record, options) {
            this._super(parent, name, record, options);
            if (this.field && this.field.type == "selection" && this.attrs.selection) {
                this.field.selection = JSON.parse(this.attrs.selection);
            }
        },
    });

});
