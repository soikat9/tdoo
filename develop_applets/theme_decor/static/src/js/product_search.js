tele.define("theme_decor.product_search", function (require) {
"use strict";

var publicWidget = require('web.public.widget');

publicWidget.registry.VougeSearchBar = publicWidget.Widget.extend({
    selector : '.tele-search, .search-box',
    events: {
        // "input .search-query-tele-tele": "_onInput",
        // "input .search-query-tele-tele-popup": "_onInput",
        // "focusout": "_onFocusOut",
        "keyup .search-query-tele": "_onKeydown",
        "keyup .search-query-tele-popup": "_onKeydown",
    },

    _onKeydown: function(ev) {
        var search_var = $(ev.currentTarget).val()
        console.log("hhhh",search_var)
        // console.log("input===",$("#tvsearchCateg").val())
        $.get("/decor/search/product", {
            'category':$("#tvsearchCateg").val(),
            'popupcateg':$("#tvsearchCateg-popup").val(),
            'term': search_var,
       }).then(function(data){
            if(data){
                $(".tele-search .tele-search-results").remove()
                $(".tele-search .tele-search-text").remove()
                $('.tele-search .o_wsale_search_order_by').after(data)
                $(".search-box .tele-search-results").remove()
                $(".search-box .tele-search-text").remove()
                $('.search-box .o_wsale_search_order_by').after(data)
            }

        });
    },
});

publicWidget.registry.tvsearchCateg = publicWidget.Widget.extend({
    "selector":".select-category, .select-category-popup",
    events:{
        "click":"_changeCategory"
    },
    _changeCategory:function(ev){
        var getcatid = $(ev.currentTarget).attr("data-id");
        var getcatname = $(ev.currentTarget).text().trim();
        $("#tvsearchCateg").val(getcatid);
        $("#categbtn > .categ-name").text(getcatname);
        $(".select-category").removeClass("text-primary");
        $(ev.currentTarget).addClass("text-primary");

        $("#tvsearchCateg-popup").val(getcatid);
        $("#categbtn-popup > .categ-name").text(getcatname);
        $(".select-category-popup").removeClass("text-primary");
        $(ev.currentTarget).addClass("text-primary");
    }
});
});

