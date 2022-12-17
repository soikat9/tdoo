/** @tele-module **/

import { GraphRenderer } from "@web/views/graph/graph_renderer";
const __themesDB = require('tele_backend_theme_ent.TeleWebThemes');
const session = require('web.session');
const userTheme = __themesDB.get_theme_config_by_uid(session.uid);
import { patch } from 'web.utils';

patch(GraphRenderer.prototype, '@tele_backend_theme_ent/static/src/js/views/graph/graph_renderer.js', {
    renderChart() {
        if (userTheme.mode === "night_mode_on") {
            Chart.defaults.global.defaultFontColor = '#f3f3f3';
            Chart.defaults.scale.gridLines.color = '#636363';
        }
        this._super(...arguments);
    },
});