{
    "name": "Iframe",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "summary": "Embed external websites as Odoo menus with app icons, parent menu placement, and company selection",
    "description": """
External Website Iframe Menu Builder
====================================

Create Odoo backend menus for external websites, portals, dashboards, and web
apps without custom coding. Configure each iframe menu with a name, URL, parent
menu, company, sequence, and custom icon.

Leave Parent Menu empty to create a top-level app menu with its own icon, or
choose an existing parent menu to place the iframe as a submenu inside Sales,
Inventory, CRM, Accounting, or any other Odoo app.

Key Features:
- Create iframe menus directly from the backend
- Open external URLs inside Odoo
- Support top-level app menus when Parent Menu is empty
- Support submenu placement under any existing Odoo menu
- Custom app icon for top-level iframe menus
- Company field for multi-company configuration
- Generated menu and action stay synced when records are edited
- Clean uninstall behavior for generated menus and actions

Note: Some websites block iframe embedding with their own security policy. This
module works with URLs that allow iframe embedding.
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["web"],
    "data": [
        "security/ir.model.access.csv",
        "views/iframe_menu_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sm_dynamic_iframe/static/src/js/iframe_action.js",
            "sm_dynamic_iframe/static/src/xml/iframe_action.xml",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [
        "static/description/banner.gif",
        "static/description/icon.png",
    ],
    "price": 49.99,
    "currency": "USD",
}
