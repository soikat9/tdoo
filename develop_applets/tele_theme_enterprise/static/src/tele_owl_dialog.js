/** @tele-module **/

import {patch} from "@web/core/utils/patch";
import {Dialog} from "@web/core/dialog/dialog";
import ThemeSetting from "tele_theme_setting.theme_setting";


patch(Dialog.prototype, "tele_owl_dialog_effect", {
    setup() {
        this._super.apply(this, arguments);
        this.dialog_pop_style = ThemeSetting.settings.dialog_pop_style;
    }
});


