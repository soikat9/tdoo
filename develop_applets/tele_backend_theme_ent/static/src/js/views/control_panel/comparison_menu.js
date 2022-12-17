tele.define("tele_backend_theme_ent.ComparisonMenu", function(require) {
    'use strict';

    const ComparisonMenu = require('web.ComparisonMenu');
    const { patch } = require('web.utils');

    patch(ComparisonMenu, 'tele_backend_theme_ent.ComparisonMenu', {

        async willStart() {
            var prom = this._super(...arguments);
            this.displayComparison = true;
            return prom;
        },
    });
});