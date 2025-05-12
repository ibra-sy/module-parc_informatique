from datetime import date, timedelta
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ContratInfogerance(models.Model):
    _name = "parc.contrat"
    _description = "Contrat d'infogérance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date_debut DESC"

    # ------------------------------------------------------------------
    # Champs Principaux
    # ------------------------------------------------------------------
    name = fields.Char(
        string="Référence", copy=False, readonly=True,
        default="Nouveau", tracking=True,
    )
    client_id = fields.Many2one(
        "parc.client", string="Client",
        required=True, tracking=True,
    )
    equipement_ids = fields.Many2many(
        "parc.equipement", string="Équipements couverts",
        domain="[('client_id', '=', client_id)]",
    )

    type_contrat = fields.Selection([
        ("standard", "Standard"),
        ("premium", "Premium"),
        ("sur_mesure", "Sur-mesure"),
    ], default="standard", required=True, tracking=True)

    frequence = fields.Selection([
        ("mensuel", "Mensuel"),
        ("trimestriel", "Trimestriel"),
        ("annuel", "Annuel"),
    ], default="mensuel", required=True, tracking=True)

    montant_ht = fields.Float(string="Montant HT", required=True, tracking=True)
    date_debut = fields.Date(required=True, default=fields.Date.today)
    date_fin = fields.Date(required=True)

    last_invoice_date = fields.Date(string="Dernière facture")
    next_invoice_date = fields.Date(
        string="Prochaine facture",
        compute="_compute_next_invoice_date", store=True,
    )

    actif = fields.Boolean(string="Contrat Actif", default=True)
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("actif", "Actif"),
        ("expire", "Expiré"),
        ("resilie", "Résilié"),
    ], default="brouillon", tracking=True)

    notes = fields.Text(string="Notes internes")

    # ------------------------------------------------------------------
    # Séquence Référence Contrat
    # ------------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "Nouveau") == "Nouveau":
                vals["name"] = self.env["ir.sequence"].next_by_code("parc.contrat") or "CTR-00000"
        records = super().create(vals_list)
        records._update_statut()
        return records

    # ------------------------------------------------------------------
    # Vérification des Dates
    # ------------------------------------------------------------------
    @api.constrains("date_debut", "date_fin")
    def _check_dates(self):
        for rec in self:
            if rec.date_fin <= rec.date_debut:
                raise ValidationError(_("La date de fin doit être postérieure à la date de début."))

    # ------------------------------------------------------------------
    # Statut Automatique
    # ------------------------------------------------------------------
    def _update_statut(self):
        today = date.today()
        for rec in self:
            if rec.statut == "actif" and rec.date_fin < today:
                rec.statut = "expire"
            elif rec.statut in ("brouillon", "expire") and rec.actif and rec.date_debut <= today < rec.date_fin:
                rec.statut = "actif"

    # ------------------------------------------------------------------
    # Prochaine Facture (Calcul Automatique)
    # ------------------------------------------------------------------
    @api.depends("date_debut", "date_fin", "frequence", "last_invoice_date")
    def _compute_next_invoice_date(self):
        freq_days = {"mensuel": 30, "trimestriel": 90, "annuel": 365}
        for rec in self:
            if rec.last_invoice_date:
                rec.next_invoice_date = rec.last_invoice_date + timedelta(days=freq_days[rec.frequence])
            else:
                rec.next_invoice_date = rec.date_debut
