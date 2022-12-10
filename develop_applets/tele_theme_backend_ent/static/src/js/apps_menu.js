/** @tele-module **/
import {fuzzyLookup} from "@web/core/utils/search";
var core = require('web.core');
var qweb = core.qweb;
var ajax = require('web.ajax');
var { NavBar } = require("@web/webclient/navbar/navbar");
var { patch } = require("web.utils");
const { useListener } = require("web.custom_hooks");

const {useState, useRef} = owl.hooks;

function AppDrawerfindNames(memo, menu) {
    if (menu.action) {
        var key = menu.parent_id ? menu.parent_id[1] + "/" : "";
        memo[key + menu.name] = menu;
    }
    if (menu.children) {
        _.reduce(menu.children, AppDrawerfindNames, memo);
    }
    return memo;
}

function findNames(memo, menu) {
    if (menu.actionID) {
        memo[menu.name.trim()] = menu;
    }
    if (menu.childrenTree) {
        const innerMemo = _.reduce(menu.childrenTree, findNames, {});
        for (const innerKey in innerMemo) {
            memo[menu.name.trim() + " / " + innerKey] = innerMemo[innerKey];
        }
    }
    return memo;
}

patch(NavBar.prototype, "tele_theme_backend.appsMenuJs", {
    setup() {
        this._super();
        
        useListener("keydown", "#app_menu_search", this._AppsearchResultsNavigate);
        useListener("input", "#app_menu_search", this._searchAppDrawerTimeout);
        useListener("click", "#search_result .search_list_content a", this._ToggleDrawer);
        useListener("click", ".fav_app_select", this._AddRemoveFavApps);
        useListener("click", ".appdrawer_section .app-box .o_app", this._ToggleDrawer);

        var menuData = this.menuService.getApps()

        this._search_def = false;

        this._GetFavouriteApps()
        this._AppdrawerIcons()
        this._FavouriteAppsIsland()

        this.state = useState({
            results: [],
            offset: 0,
            hasResults: false,
        });

        this.searchBarInput = useRef("SearchBarInput");
        this._drawersearchableMenus = [];
        for (const menu of this.menuService.getApps()) {
            Object.assign(
                this._drawersearchableMenus,
                _.reduce([this.menuService.getMenuAsTree(menu.id)], findNames, {})
            );
        }
        $('.o_main_navbar').removeClass('d-none')


        $('.favorite_apps_section').scroll(function(){
            if ($('.favorite_apps_section').scrollTop() > 20) {
                $('.favorite_apps_section').css( { height: `calc(100vh - ${sidebar_systray_height}px)` } );
            } else {
                $('.favorite_apps_section').css( { height: `calc(100vh - ${sidebar_systray_height}px)` } );
            }
        });
    },

    _ToggleDrawer: function (ev) {
        $('.o_main_navbar').toggleClass('appdrawer-toggle')
        $('.appdrawer_section').toggleClass('toggle')
        $('.o_app_drawer a').toggleClass('toggle')

        if (!$('.appdrawer_section').hasClass('toggle')) {
            $("input[id='app_menu_search']").val("")
            $(".appdrawer_section #search_result").empty()
            $('.appdrawer_section .apps-list .row').removeClass('d-none');
            $('#searched_main_apps').empty().addClass('d-none').removeClass('d-flex');
        }
    },

    _FavouriteAppsIsland: function (ev){
        ajax.rpc('/get-favorite-apps').then(function(rec) {
            if (rec.app_list.length) {
                $('.fav_app_island .fav_apps').empty();
                $.each(rec.app_list, function( index, value ) {
                    var favapps = $(qweb.render("FavoriteApps", {
                        app_name:value['name'],
                        app_id:value['app_id'],
                        app_xmlid:value['app_xmlid'],
                        app_actionid:value['app_actionid'],
                        use_icon:value['use_icon'],
                        icon_class_name:value['icon_class_name'],
                        icon_img:value['icon_img'],
                        web_icon:value['web_icon'],
                        web_icon_data:value['web_icon_data'],
                    }))
                    $('.fav_app_island .fav_apps').append(favapps)
                });
                $('.fav_app_island').removeClass('d-none')
            } else {
                $('.fav_app_island').addClass('d-none')
            }
        });
    },

    _GetFavouriteApps: function() {
        var apps = this.menuService.getApps()
        ajax.rpc('/get-favorite-apps').then(function(rec) {
            if (rec) {
                $.each(rec.app_list, function( index, value ) {
                    $.each(apps, function( ind, val ) {
                        if (value['app_id'] == val.id) {
                            var target = ".o_app[data-menu-id="+val.id+"]";
                            var $target = $(target);
                            $target.parent().find('.fav_app_select .ri').addClass('active');
                        }
                    });
                });
            }
        });
    },

    get_user_data: function (ev) {
        var self = this
        var session = this.getSession();
        var $avatar = $('.user_image img');
        var avatar_src = session.url('/web/image', {
            model:'res.users',
            field: 'image_128',
            id: session.uid,
        });
        var current_time_hr = new Date().getHours().toLocaleString("en-US", { timeZone: session.user_context.tz });
        if (parseInt(current_time_hr) < 12){
            var greeting = "Good Morning"
        } else if ((parseInt(current_time_hr) >= 12) && parseInt(current_time_hr) <= 17) {
            var greeting = "Good Afternoon"
        } else if (parseInt(current_time_hr) >= 17){
            var greeting = "Good Evening"
        }
        var value = {
            'avatar_src': avatar_src,
            'user_id': session.uid,
            'user_name': session.name,
            'greeting': greeting,
        }
        $avatar.attr('src', avatar_src);
        return value
    },

    _AddRemoveFavApps: function (ev) {
        var self = this 
        var app_id = $(ev.target).parent().find('.o_app').attr('data-menu-id')
        var app_name = $(ev.target).parent().find('.app-name').text()
        if ($(ev.target).find('.ri.active').length) {
            ajax.jsonRpc('/remove-user-fav-apps','call', {
                'app_id':app_id,
            }).then(function(rec) {
                $(ev.target).find('.ri').removeClass('active');
                self._FavouriteAppsIsland()
            });
        } else {
            ajax.jsonRpc('/update-user-fav-apps','call', {
                'app_name':app_name,
                'app_id':app_id,
            }).then(function(rec) {
                $(ev.target).find('.ri').addClass('active');
                self._FavouriteAppsIsland()
            });
        }
    },

    _getsearchedapps: function(searchvals) {
        var self = this
        var apps = this.menuService.getApps()
        if (searchvals === "") {
            $('#searched_main_apps').empty().addClass('d-none').removeClass('d-flex');
            return;
        }
        $('#searched_main_apps').empty().addClass('d-flex').removeClass('d-none');
        $.each(apps, function( index, value ) {
            if(value['name'].toLowerCase().indexOf(searchvals.toLowerCase()) != -1){
                var searchapps = $(qweb.render("SearchedApps", {
                    app_name:value['name'],
                    app_id:value['menuID'],
                    app_xmlid:value['xmlID'],
                    app_actionid:value['actionID'],
                }))
                if (value['use_icon']) {
                    if (value['icon_class_name']) {
                        var icon_span = "<span class='ri "+value['icon_class_name']+"'/>"
                        $(searchapps).find('.app-image').append($(icon_span))
                    } else if (value['icon_img']) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value['id']+"/icon_img' />"
                        $(searchapps).find('.app-image').append($(icon_image))
                    } else if (value['webIconData']) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value['id']+"/web_icon_data' />"
                        $(searchapps).find('.app-image').append($(icon_image))
                    } else {
                        var icon_span = "<span class='"+value.webIcon.iconClass+"'style='background-color:"+value.webIcon.backgroundColor+"; color: "+value.webIcon.color+" '/>"
                        $(searchapps).find('.app-image').append($(icon_span))
                    }
                } else {
                    if (value['icon_img']) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value['id']+"/icon_img' />"
                        $(searchapps).find('.app-image').append($(icon_image))
                    } else if (value['webIconData']) {
                        var icon_image = "<img class='img img-fluid' src='/web/image/ir.ui.menu/"+value['id']+"/web_icon_data' />"
                        $(searchapps).find('.app-image').append($(icon_image))
                    } else {
                        var icon_span = "<span class='"+value.webIcon.iconClass+"'style='background-color:"+value.webIcon.backgroundColor+"; color: "+value.webIcon.color+" '/>"
                        $(searchapps).find('.app-image').append($(icon_span))
                    }
                }
                $('.apps-list #searched_main_apps').append(searchapps);
            }
        });
        this._GetFavouriteApps();
    },

    _AppsearchResultsNavigate: function(ev) {
        // Find current results and active element (1st by default)
        const all = $(".appdrawer_section #search_result").find(".search_list_content"),
            pre_focused = all.filter(".navigate_active") || $(all[0]);
        let offset = all.index(pre_focused),
            key = ev.key;
        // Keyboard navigation only supports search results
        if (!all.length) {
            return;
        }
        // Transform tab presses in arrow presses
        if (key === "Tab") {
            ev.preventDefault();
            key = ev.shiftKey ? "ArrowUp" : "ArrowDown";
        }
        switch (key) {
            // Pressing enter is the same as clicking on the active element
            case "Enter":
                $(pre_focused).find('.autoComplete_highlighted')[0].click();
                break;
            // Navigate up or down
            case "ArrowUp":
                offset--;
                break;
            case "ArrowDown":
                offset++;
                break;
            default:
                // Other keys are useless in this event
                return;
        }
        // Allow looping on results
        if (offset < 0) {
            offset = all.length + offset;
        } else if (offset >= all.length) {
            offset -= all.length;
        }
        // Switch active element
        const new_focused = $(all[offset]);
        pre_focused.removeClass("navigate_active");
        new_focused.addClass("navigate_active");
        $(".appdrawer_section #search_result").scrollTo(new_focused, {
            offset: {
                top: $(".appdrawer_section #search_result").height() * -0.5,
            },
        });
    },

    _menuInfo(key) {
        return this._drawersearchableMenus[key];
    },

    _searchAppDrawerTimeout: function (ev) {
        this._search_def = new Promise((resolve) => {
            setTimeout(resolve, 100);
        });
        this._search_def.then(this._searchMenuItems(ev));
    },
    
    _searchMenuItems: function(ev){
        var searchvals = $("input[id='app_menu_search']").val()
        this._getsearchedapps(searchvals);
        $(".appdrawer_section .apps-list .row").toggleClass('d-none',Boolean(searchvals.length));
        if (searchvals === "") {
            $(".appdrawer_section #search_result").empty();
            $(".appdrawer_section #searched_main_apps").empty().removeClass('d-flex').addClass('d-none');
            return;
        }
        const query = ev.srcElement.value;
        this.state.hasResults = query !== "";
        var results = this.state.hasResults
            ? fuzzyLookup(searchvals, _.keys(this._drawersearchableMenus), (k) => k)
            : [];
        $(".appdrawer_section #search_result").html(
            core.qweb.render("tele_theme_backend_ent.MenuSearchResults", {
                results: results,
                widget: this,
            })
        );
    },

    _AppdrawerIcons: function() {
        var self = this
        var apps = this.menuService.getApps()
        $.each(apps, function( key, value ) {
            ajax.jsonRpc('/get/irmenu/icondata','call', {
                'menu_id':value.id,
            }).then(function(rec) {
                var target_tag = '.appdrawer_section a.o_app[data-menu-id='+rec[0].id+']'
                var $tagtarget = $(target_tag)
                $tagtarget.find('.app-image').empty()

                value.id = rec[0].id
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
            })
        });
    },
});