/** @tele-module **/

import { registry } from "@web/core/registry";
import { AppBoard } from "./tele_app_board";

const { core } = owl;
const { EventBus } = core;


export const TeleAppboardService = {
    dependencies: ["menu"],

    start() {
        const bus = new EventBus();
        registry.category("main_components").add("TeleAppBoard", {
            Component: AppBoard,
            props: {
                bus: bus
            },
        });

        return {
            show: () => {
                bus.trigger("ShowAppBoard");
            },

            hide: () => {
                bus.trigger("HideAppBoard");
            }
        }
    }
};

registry.category("services").add("tele_app_board", TeleAppboardService);
