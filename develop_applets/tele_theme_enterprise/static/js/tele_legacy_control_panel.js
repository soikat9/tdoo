tele.define('tele_theme_enterprise.ControlPanel', function (require) {
    "use strict";

    const ControlPanel = require('web.ControlPanel')
    const { patch } = require("web.utils");
    const config = require('web.config')
    const search_options = require('tele_theme_enterprise.search_options')

    const TeleFilterMenu = search_options.TeleFilterMenu
    const TeleGroupMenu = search_options.TeleGroupMenu
    const TeleFavoriteMenu = search_options.TeleFavoriteMenu
    const TeleComparisonMenu = search_options.TeleComparisonMenu

    const { misc, hooks} = owl;
    const { Portal } = misc;
    const { useState } = hooks;
    const { useExternalListener, useRef } = hooks;

    patch(ControlPanel.prototype, "tele_theme_enterprise_control_panel", {

        setup() {
            this._super.apply(this, arguments);
    
            // check if it is mobile device
            let isMobile = false;
            if (config.device.isMobile) {
                isMobile = true;
            } else {
                isMobile = false;
            }

            this.state = useState({
                "isMobile": isMobile,
                "mobile_search_bar_visible": false
            })
    
            config.device.bus.on('size_changed', this, () => {
                if (config.device.isMobile) {
                    this.state.isMobile = true;
                } else {
                    this.state.isMobile = false;
                }
            });

            this.optionDropDown = useRef('optionDropDown');
            this.mobileOptionDropDown = useRef('mobileOptionDropDown');

            useExternalListener(window, 'click', this._hideOptions);
        },

        get_active_view_icon(env) {
            var activeView = _.findWhere(this.props.views, { type: env.view.type });
            return activeView.icon
        },

        _OptionDropdownToggleClick(event) {
            this.optionDropDown.el.classList.add('show');
        },

        _MobileOptionDropdownToggleClick(event) {
            this.mobileOptionDropDown.el.classList.add('show');
        },

        _hideOptions(event) {
            if (this.state.isMobile) {
                if (!this.mobileOptionDropDown.el) {
                    return
                }
            } else {
                if (!this.optionDropDown.el) {
                    return
                }
            }

            // check if it need to hide the option
            if (!$(event.target).is(
                $(".tele_search_option_dropdown, .tele_search_option_dropdown *, .search_option_dropdown_toggler"))) 
            {
                if (this.state.isMobile) {
                    this.mobileOptionDropDown.el.classList.remove('show');
                } else {
                    this.optionDropDown.el.classList.remove('show');
                }
            }
        },

        on_mobile_search_bar_toggle_click() {
            this.state.mobile_search_bar_visible = !this.state.mobile_search_bar_visible;
        }
    });

    ControlPanel.defaultProps = {
        ...ControlPanel.defaultProps,
        isActive: true,
        isInDialog: false
    }

    ControlPanel.props = {...ControlPanel.props, isActive: Boolean, isInDialog: Boolean}
    ControlPanel.components = {...ControlPanel.components, Portal, TeleFilterMenu, TeleGroupMenu, TeleFavoriteMenu, TeleComparisonMenu}
});
