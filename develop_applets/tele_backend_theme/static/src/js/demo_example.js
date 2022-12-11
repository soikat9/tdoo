tele.define('tele_backend_theme.name_of_fetures', function (require) {
    'use strict';
    var core = require('web.core');
    var ajax = require('web.ajax');
    var qweb = core.qweb;
    ajax.loadXML('/tele_backend_theme/views/tele_theme_setting.xml', qweb);
    });