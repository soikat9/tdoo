tele.define('tele_theme_enterprise.search_options', function (require) {
    "use strict";

    const FilterMenu = require('web.FilterMenu')
    const GroupByMenu = require('web.GroupByMenu')
    const FavoriteMenu = require('web.FavoriteMenu')
    const ComparisonMenu = require('web.ComparisonMenu')

    class TeleFilterMenu extends FilterMenu {}
    TeleFilterMenu.template = "tele_theme_enterprise.legacy.FilterMenu"

    class TeleGroupMenu extends GroupByMenu {}
    TeleGroupMenu.template = "tele_theme_enterprise.GroupByMenu"

    class TeleFavoriteMenu extends FavoriteMenu {}
    TeleFavoriteMenu.template = "tele_theme_enterprise.FavoriteMenu"

    class TeleComparisonMenu extends ComparisonMenu {}
    TeleComparisonMenu.template = "tele_theme_enterprise.ComparisonMenu"

    return {
        TeleFilterMenu,
        TeleGroupMenu,
        TeleFavoriteMenu,
        TeleComparisonMenu
    }
})