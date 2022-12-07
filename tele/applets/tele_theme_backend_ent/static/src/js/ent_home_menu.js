/** @tele-module **/
import { HomeMenu } from "@web_enterprise/webclient/home_menu/home_menu";
import { BurgerMenu } from "@web_enterprise/webclient/burger_menu/burger_menu";
var { registry } = require("@web/core/registry");
var { patch } = require("web.utils");
var ajax = require('web.ajax');

patch(HomeMenu.prototype, "tele_theme_backend_ent.entHomeMenuJs", {
    setup() {
        $('body').addClass('d-none');
        this._super();
        var apps = this.availableApps
        $.each(apps, function( key, value ) {
            ajax.jsonRpc('/get/irmenu/icondata','call', {
                'menu_id':value.id,
            }).then(function(rec) {
                var target_tag = '.o_home_menu_scrollable a.o_app[id=result_app_'+key+']'
                var $tagtarget = $(target_tag)
                $tagtarget.find('.app-image').empty()

                value.use_icon = rec[0].use_icon
                value.icon_class_name = rec[0].icon_class_name
                value.icon_img = rec[0].icon_img


                if (rec[0].use_icon) {
                    if (rec[0].icon_class_name) {
                        var icon_span = "<span class='ri "+rec[0].icon_class_name+"'/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    } else if (rec[0].icon_img) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+rec[0].id+"/icon_img' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else if (rec[0].web_icon_data) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+rec[0].id+"/web_icon_data' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else {
                        var icon_data = rec[0].web_icon.split(',')
                        var icon_span = "<span class='"+icon_data[0]+"'style='background-color:"+icon_data[2]+"; color: "+icon_data[1]+" '/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    }
                } else {
                    if (rec[0].icon_img) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+rec[0].id+"/icon_img' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else if (rec[0].web_icon_data) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+rec[0].id+"/web_icon_data' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else {
                        var icon_data = rec[0].web_icon.split(',')
                        var icon_span = "<span class='"+icon_data[0]+"'style='background-color:"+icon_data[2]+"; color: "+icon_data[1]+" '/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    }
                }
                $tagtarget.removeClass('d-none')
            })
        });
    },
    patched() {
        this._super();
        var apps = this.availableApps
        $.each(apps, function( key, value ) {
                var target_tag = '.o_home_menu_scrollable a.o_app[id=result_app_'+key+']'
                var $tagtarget = $(target_tag)
                $tagtarget.find('.app-image').empty()
                if (value.use_icon) {
                    if (value.icon_class_name) {
                        var icon_span = "<span class='ri "+value.icon_class_name+"'/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    } else if (value.icon_img) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value.id+"/icon_img' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else if (value.webIconData) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value.id+"/web_icon_data' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else {
                        var icon_span = "<span class='"+value.webIcon.iconClass+"'style='background-color:"+value.webIcon.backgroundColor+"; color: "+value.webIcon.color+" '/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    }
                } else {
                    if (value.icon_img) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value.id+"/icon_img' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else if (value.webIconData) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value.id+"/web_icon_data' />"
                        $tagtarget.find('.app-image').append($(icon_image))
                    } else {
                        var icon_span = "<span class='"+value.webIcon.iconClass+"'style='background-color:"+value.webIcon.backgroundColor+"; color: "+value.webIcon.color+" '/>"
                        $tagtarget.find('.app-image').append($(icon_span))
                    }
                }
                $tagtarget.removeClass('d-none')
        });
    },
    willUnmount() {
        $('body').css("background-image", "")
    },
});
patch(BurgerMenu.prototype, "tele_theme_backend_ent.entBurgerMenuJs", {
    setup() {
        this._super();
        var size = $(window).width();
        if (size <= 1200) {
            this.env.isSmalldevice = true;
        } else {
            this.env.isSmalldevice = false;
        }
    }
});

const systrayItem = {
    Component: BurgerMenu,
    isDisplayed: (env) => {
        var size = $(window).width();
        if (size < 992) {
            return true;
        } else {
            return false;
        }
    },
};

registry.category("systray").add("burger_menu", systrayItem, { sequence: 0, force: true });
