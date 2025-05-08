from odoo import models, fields, api

class Intervention(models.Model):
    _name = 'parc.intervention'
    _description = "Intervention technique"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_ouverture desc'

    name = fields.Char(string="Référence", default="Nouveau", readonly=True, copy=False)
    client_id = fields.Many2one('parc.client', string="Client", required=True)
    equipement_id = fields.Many2one('parc.equipement', string="Équipement concerné")
    technicien_id = fields.Many2one('res.users', string="Technicien assigné", domain="[('share', '=', False)]")
    date_ouverture = fields.Datetime(string="Date d'ouverture", default=fields.Datetime.now)
    date_cloture = fields.Datetime(string="Date de clôture")
    description = fields.Text(string="Description de l'incident")
    diagnostic = fields.Text(string="Diagnostic / Résolution")
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
        ('ferme', 'Fermé')
    ], default='brouillon', string="Statut", tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name') == 'Nouveau':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.intervention') or 'INT-00000'
        return super().create(vals)
