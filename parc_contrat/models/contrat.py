from odoo import models, fields, api
from datetime import date, timedelta

class ContratInfogerance(models.Model):
    _name = 'parc.contrat'
    _description = "Contrat d'infogérance"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_debut desc'

    name = fields.Char(string="Référence contrat", required=True, copy=False, readonly=True, default='Nouveau')
    client_id = fields.Many2one('parc.client', string="Client", required=True, tracking=True)
    equipement_ids = fields.Many2many('parc.equipement', string="Équipements couverts", domain="[('client_id', '=', client_id)]")

    type_contrat = fields.Selection([
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('sur_mesure', 'Sur mesure')
    ], string="Type de contrat", required=True, default='standard')

    date_debut = fields.Date(string="Date de début", required=True, default=fields.Date.today)
    date_fin = fields.Date(string="Date de fin", required=True)

    frequence = fields.Selection([
        ('mensuel', 'Mensuel'),
        ('trimestriel', 'Trimestriel'),
        ('annuel', 'Annuel')
    ], string="Fréquence de facturation", required=True, default='mensuel')

    montant_ht = fields.Float(string="Montant HT (XOF)", required=True)
    actif = fields.Boolean(string="Actif", default=True)

    statut = fields.Selection([
        ('brouillon', 'Brouillon'),
        ('actif', 'Actif'),
        ('expire', 'Expiré'),
        ('resilie', 'Résilié')
    ], string="Statut", default='brouillon', tracking=True)

    notes = fields.Text(string="Conditions particulières")

    # Générer automatiquement la référence du contrat
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nouveau') == 'Nouveau':
            vals['name'] = self.env['ir.sequence'].next_by_code('parc.contrat') or 'CTR-00000'
        return super().create(vals)

    # Vérifie et met à jour le statut automatiquement si date expirée
    def write(self, vals):
        result = super().write(vals)
        for record in self:
            record._update_statut()
        return result

    @api.depends('date_fin')
    def _update_statut(self):
        today = fields.Date.today()
        for contrat in self:
            if contrat.statut == 'actif' and contrat.date_fin and contrat.date_fin < today:
                contrat.statut = 'expire'
