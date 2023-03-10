
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Let's Encrypt",
    "version": "1.0.1.0.1",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Request SSL certificates from letsencrypt.org",
    "depends": ["base_setup"],
    "data": [
        "data/ir_config_parameter.xml",
        "data/ir_cron.xml",
        "views/res_config_settings.xml",
    ],
    "demo": ["demo/ir_cron.xml"],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "external_dependencies": {
        "python": ["acme", "cryptography", "dnspython", "josepy"]
    },
}
