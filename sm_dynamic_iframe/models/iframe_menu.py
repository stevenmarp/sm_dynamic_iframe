import base64

from odoo import api, fields, models
from odoo.tools.misc import file_open


class SmIframeMenu(models.Model):
    _name = "sm.iframe.menu"
    _description = "Dynamic Iframe Menu"
    _order = "sequence, id"

    name = fields.Char(required=True)
    url = fields.Char(string="External URL", required=True)
    parent_menu_id = fields.Many2one(
        "ir.ui.menu", string="Parent Menu",
        help="Leave empty to create a top-level app menu.",
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )
    sequence = fields.Integer(default=10)
    icon_image = fields.Binary(
        string="Menu Icon",
        attachment=True,
        default=lambda self: self._default_icon_image(),
        help="Optional icon for generated top-level app menu.",
    )
    menu_id = fields.Many2one("ir.ui.menu", string="Generated Menu", readonly=True, copy=False)
    action_id = fields.Many2one("ir.actions.client", string="Generated Action", readonly=True, copy=False)

    def _default_icon_image(self):
        with file_open("sm_dynamic_iframe/static/description/icon.png", "rb") as icon_file:
            return base64.b64encode(icon_file.read())

    def _sync_action_menu(self):
        Client = self.env["ir.actions.client"]
        Menu = self.env["ir.ui.menu"]
        for rec in self:
            action_vals = {
                "name": rec.name,
                "tag": "sm_dynamic_iframe",
                "params": {"url": rec.url, "company_id": rec.company_id.id},
            }
            action = rec.action_id
            if action:
                action.write(action_vals)
            else:
                action = Client.create(action_vals)
            menu_vals = {
                "name": rec.name,
                "parent_id": rec.parent_menu_id.id or False,
                "action": "ir.actions.client,%d" % action.id,
                "sequence": rec.sequence,
            }
            if rec.parent_menu_id:
                menu_vals.update({"web_icon": False, "web_icon_data": False})
            elif rec.icon_image:
                menu_vals["web_icon_data"] = rec.icon_image
            else:
                menu_vals.update({
                    "web_icon": "sm_dynamic_iframe,static/description/icon.png",
                    "web_icon_data": False,
                })
            menu = rec.menu_id
            if menu:
                menu.write(menu_vals)
            else:
                menu = Menu.create(menu_vals)
            if not rec.parent_menu_id and rec.icon_image and menu.web_icon:
                menu.write({"web_icon": False})
                menu.write({"web_icon_data": rec.icon_image})
            rec.with_context(skip_sync=True).write({"action_id": action.id, "menu_id": menu.id})

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._sync_action_menu()
        return records

    def write(self, vals):
        res = super().write(vals)
        if not self.env.context.get("skip_sync"):
            self._sync_action_menu()
        return res

    def unlink(self):
        menus = self.menu_id
        actions = self.action_id
        res = super().unlink()
        menus.unlink()
        actions.unlink()
        return res
