from odoo import models, fields

class Equipement(models.Model):
    _name = 'parc.equipement'
    _description = "Équipement IT"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_acquisition desc'

    name = fields.Char(string="Désignation", required=True, tracking=True)
    reference = fields.Char(string="Référence", readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('parc.equipement'))
    type = fields.Selection([
        ('ordinateur', 'Ordinateur'),
        ('imprimante', 'Imprimante'),
        ('routeur', 'Routeur'),
        ('serveur', 'Serveur'),
        ('logiciel', 'Licence / Logiciel'),
        ('autre', 'Autre')
    ], string="Type", required=True)
    marque = fields.Char(string="Marque")
    modele = fields.Char(string="Modèle")
    numero_serie = fields.Char(string="N° Série")
    date_acquisition = fields.Date(string="Date d'acquisition", default=fields.Date.today)
    garantie_fin = fields.Date(string="Fin de garantie")
    etat = fields.Selection([
        ('en_service', 'En service'),
        ('en_panne', 'En panne'),
        ('remplace', 'Remplacé'),
        ('hors_service', 'Hors service')
    ], default='en_service', string="État", tracking=True)

    client_id = fields.Many2one('parc.client', string="Client", required=True)
    site_id = fields.Many2one('parc.client.site', string="Site", domain="[('client_id', '=', client_id)]")
    description = fields.Text()
