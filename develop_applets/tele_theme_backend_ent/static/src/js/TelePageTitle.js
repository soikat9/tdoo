tele.define('tele_theme_backend_ent.TelePageTitle', function (require) {
"use strict";

    var ajax = require('web.ajax');
    var { WebClient } = require("@web/webclient/webclient");
    var { patch } = require("web.utils");

    patch(WebClient.prototype, "tele_theme_backend_ent.TelePageTitle", {
        setup() {
            this._super();
            var self = this
            ajax.rpc('/get/tab/title/').then(function(rec) {
                var new_title = rec
                self.title.setParts({ ztele: new_title })
            })
        },
    });
});