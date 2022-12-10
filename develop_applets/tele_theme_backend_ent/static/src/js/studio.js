/** @tele-module **/

var { StudioClientAction } = require("@tele_studio/client_action/studio_client_action");
var { patch } = require("web.utils");

patch(StudioClientAction.prototype, "tele_theme_backend.StudioClientJs", {
    mounted() {
        this._super();
        this.isverticalmenu = false;
        if ($('body').hasClass('top_menu_vertical')) {
            $('body').removeClass('top_menu_vertical');
            $('body').addClass('top_menu_horizontal');
            this.isverticalmenu = true;
        }
    },
    willUnmount() {
        this._super();
        if (this.isverticalmenu) {
            $('body').removeClass('top_menu_horizontal');
            $('body').addClass('top_menu_vertical');
        }
    }
});