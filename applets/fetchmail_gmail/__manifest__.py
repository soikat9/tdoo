# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

{
    "name": "Fetchmail Gmail",
    "version": "1.0",
    "category": "Hidden",
    "description": "Google authentication for incoming mail server",
    "depends": [
        "google_gmail",
        "fetchmail",
    ],
    "data": ["views/fetchmail_server_views.xml"],
    "auto_install": True,
    "license": "LGPL-3",
}
