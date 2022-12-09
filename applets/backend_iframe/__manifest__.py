# -*- encoding: utf-8 -*-
##############################################################################
#    This module allows Clients to view external content through backend iframes
##############################################################################
{
    'name': "Iframes Backend Dashboard",
    'summary': """This module allows Clients to view external content through backend iframes.""",
    'description': """
        This module allows Clients to view external content through backend iframes.
    """,
    'version': '1.0',
    'category': 'Dashboards',
    'license': 'TPL-1',
    'website': "",
    'contributors': [
    ],
    'support': 'support@tele.studio',
    'depends': [
        'base',
        'web',
        'mail',
        'board',
    ],
    'data': [
        'security/backend_iframe_access_rules.xml',
        'security/ir.model.access.csv',
        'views/backend_iframe.xml',
    ],
'assets': {
        'web.assets_backend': [
            '/backend_iframe/static/src/js/iframe.js',
        ]},
    'images': [
        ''
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,

}
