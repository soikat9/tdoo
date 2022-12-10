/** @tele-module **/

import { registry } from "@web/core/registry";
import { TeleOverlay } from "./tele_overlay";

const { core } = owl;
const { EventBus } = core;


export const TeleOverlayService = {

    start() {
        const bus = new EventBus();

        registry.category("main_components").add("Overlay", {
            Component: TeleOverlay,
            props: { bus },
        });

        function show(zIndex) {
            bus.trigger("Show", {
                zIndex: zIndex
            });
        }

        function hide() {
            bus.trigger("Hide");
        }

        return {
            show,
            hide
        }
    }
};

registry.category("services").add("tele_overlay", TeleOverlayService);
