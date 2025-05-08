# parc_client/models/client.py
from odoo import models, fields, api

class ClientEntreprise(models.Model):
    _name = "parc.client"
    _description = "Client Entreprise"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ['mail.thread', 'mail.activity.mixin']   # ← remis
    _order = "name"

    partner_id  = fields.Many2one("res.partner", required=True,
                                  ondelete="cascade")

    # champs spécifiques
    responsable = fields.Char(string="Responsable", tracking=True)
    siret       = fields.Char(string="SIRET / NIF")
    site_ids    = fields.One2many("parc.client.site", "client_id")

    # alias (types cohérents)
    name      = fields.Char(related="partner_id.name",  readonly=False)
    email     = fields.Char(related="partner_id.email", readonly=False)
    telephone = fields.Char(related="partner_id.phone", readonly=False)
    adresse   = fields.Char(related="partner_id.street", readonly=False)

    @api.model
    def create(self, vals):
        if not vals.get("partner_id"):
            vals["partner_id"] = self.env["res.partner"].create({
                "name":  vals.get("name"),
                "email": vals.get("email"),
                "phone": vals.get("telephone"),
                "street": vals.get("adresse"),
                "is_company": True,
            }).id
        return super().create(vals)
