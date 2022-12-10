/**
 * company editor action
 */
tele.define('tele.theme_edit_action', function (require) {
    "use strict";

    var core = require('web.core');

    /**
     * @param {*} parent
     * @param {*} action
     */
    function show_theme_editor(env, action) {
        core.bus.trigger('tele_show_theme_editor', action);
    }

    core.action_registry.add('theme_edit_action', show_theme_editor);
});