/** @tele-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class TeleSystray extends owl.Component {

    setup() {
        this.hm = useService("tele_app_board");
        this.studio = useService("studio");
        this.env.bus.on("ACTION_MANAGER:UI-UPDATED", this, (mode) => {
            if (mode !== "new") {
                this.render();
            }
        });
    }

    get buttonDisabled() {
        return !this.studio.isStudioEditable();
    }
    
    _onClick() {
        this.studio.open();
    }
}

// replace the systray item
TeleSystray.template = "tele_theme_studio_patch.SystrayItem";

export const systrayItem = {
    Component: TeleSystray,
    isDisplayed: (env) => env.services.user.isSystem,
};

registry.category("systray").add("TeleSystrayItem", systrayItem, { sequence: 1 });
