# -*- coding: utf-8 -*-
from odoo import models, fields

class ClientSite(models.Model):
    _name = "parc.client.site"
    _description = "Site du client"

    name      = fields.Char(string="Nom du site", required=True)
    adresse   = fields.Text(string="Adresse")
    client_id = fields.Many2one(
        "parc.client", string="Client", required=True, ondelete="cascade")
