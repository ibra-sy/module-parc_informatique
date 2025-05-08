from odoo import models, fields

# parc_client/models/site.py
class ClientSite(models.Model):
    _name = "parc.client.site"
    _description = "Site du client"

    name      = fields.Char(required=True)
    adresse   = fields.Text()
    client_id = fields.Many2one("parc.client", required=True, ondelete="cascade")

