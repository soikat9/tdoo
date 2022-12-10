tele.define('dynamic_tele.jquery.extensions', function () {
'use strict';

    var propRowIndex = $.fn.prop;

    $.fn.extend({
        prop: function( name, value ) {
            let result = propRowIndex.apply(this, arguments);
            if (name === "rowIndex") {
                var tableCheck = this.parents(".o_list_table");
                if (tableCheck.length) {
                    result -= tableCheck.find(".searchAdvance").length ? 1 : 0;
                }
            }
            return result;
        },
    });
});
