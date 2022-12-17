/** @tele-module **/

import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';

var HelperMenu = Widget.extend({
    name: 'helper_menu',
    template: 'tele_backend_theme_ent.SystrayHepler',
});

SystrayMenu.Items.push(HelperMenu);
export default HelperMenu;