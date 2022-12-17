/** @tele-module */

import { BurgerMenu } from "@web_enterprise/webclient/burger_menu/burger_menu";
import { registry } from "@web/core/registry";
/**
 * The user menu in enterprise should be removed if the screen is small
 * It is handled by the burger menu.
 */
registry.category("systray").remove("burger_menu");