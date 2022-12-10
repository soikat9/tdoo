/** @tele-module **/


const { Component, hooks, QWeb } = owl;
const { useState } = hooks;


export class TeleAccordion extends Component {

    setup() {
        this.state = useState({
            'collapse': true
        })
    }

    toggleDisplay() {
        this.state.collapse = !this.state.collapse;
    }
}

TeleAccordion.props = {
    title: {
        type: String
    }
};
TeleAccordion.template = "tele_theme_enterprise.accordion";
TeleAccordion.components = {};

QWeb.registerComponent("TeleAccordion", TeleAccordion);
