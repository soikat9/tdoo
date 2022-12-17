/** @tele-module **/

var __themesDB = require('tele_backend_theme_ent.TeleWebThemes');
var session = require('web.session');

// Added Global
window['TeleTheme'] = __themesDB.get_theme_config_by_uid(session.uid);