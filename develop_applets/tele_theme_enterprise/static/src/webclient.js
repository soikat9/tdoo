/** @tele-module **/

import { SideBarMenu } from "./components/sidebar_menu/tele_sidebar_menu";
import { TeleHeader } from "./components/header/tele_header";
import { TeleFooter } from "./components/footer/tele_footer";
import { WebClient }  from '@web/webclient/webclient';


export class TeleWebClient extends WebClient {}

TeleWebClient.components = {
    ...WebClient.components,
    SideBarMenu,
    TeleFooter,
    TeleHeader
};
