from odoo import models, fields, api
from datetime import timedelta

class FactureContrat(models.Model):
    _name = 'parc.facture'
    _description = "Facture automatique contrat"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_facture desc'

    name = fields.Char(string="Référence", required=True, default="Nouveau", copy=False, readonly=True)
    contrat_id = fields.Many2one('parc.contrat', string="Contrat", required=True)
    client_id = fields.Many2one(related='contrat_id.client_id', string="Client", store=True)
    montant = fields.Float(string="Montant (XOF)", compute='_compute_montant', store=True)
    date_facture = fields.Date(string="Date de facturation", default=fields.Date.today)
    etat = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('envoye', 'Envoyé'),
        ('paye', 'Payé')
    ], default='brouillon', string="Statut", tracking=True)

    @api.depends('contrat_id')
    def _compute_montant(self):
        for rec in self:
            rec.montant = rec.contrat_id.montant_ht or 0.0

    @api.model
    def create(self, vals):
        if vals.get('name') == 'Nouveau':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.facture') or 'FAC-00000'
        return super().create(vals)

    @api.model
    def _generer_factures_periodiques(self):
        today = fields.Date.today()
        contrats = self.env['parc.contrat'].search([('actif', '=', True), ('statut', '=', 'actif')])

        for contrat in contrats:
            # Récupérer la dernière facture
            derniere = self.search([('contrat_id', '=', contrat.id)], order='date_facture desc', limit=1)
            if derniere:
                ecart = (today - derniere.date_facture).days
            else:
                ecart = (today - contrat.date_debut).days

            doit_facturer = (
                (contrat.frequence == 'mensuel' and ecart >= 30) or
                (contrat.frequence == 'trimestriel' and ecart >= 90) or
                (contrat.frequence == 'annuel' and ecart >= 365)
            )

            if doit_facturer:
                self.create({'contrat_id': contrat.id})
