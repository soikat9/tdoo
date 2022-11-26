/** @tele-module **/

import { TeleFullScreen } from '../full_screen/tele_full_screen';
import config from 'web.config';

const { Component, hooks } = owl;
const { useState } = hooks;


export class TeleFooter extends Component {

    setup() {
        super.setup();
        this.state = useState({ 
            isMobile: config.device.isMobile? true : false 
        });
        config.device.bus.on('size_changed', this, this._onDeviceSizeChanged);
    }

    _onDeviceSizeChanged() {
        this.state.isMobile = config.device.isMobile? true : false
    }
}

TeleFooter.components = {
    TeleFullScreen
};

TeleFooter.defaultProps = {};
TeleFooter.props = {};
TeleFooter.template = 'tele_theme_enterprise.footer';
