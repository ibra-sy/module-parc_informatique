from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date


class FactureContrat(models.Model):
    _name = "parc.facture"
    _description = "Facture automatique – Infogérance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "date_facture DESC"

    # -----------------------------------------------------------------
    # Champs principaux
    # -----------------------------------------------------------------
    name = fields.Char(
        string="Référence", readonly=True, copy=False,
        default="Nouveau"
    )
    contrat_id = fields.Many2one(
        "parc.contrat", string="Contrat", required=True, ondelete="cascade"
    )
    client_id = fields.Many2one(
        related="contrat_id.client_id", store=True, readonly=True
    )

    date_facture = fields.Date(default=fields.Date.today)
    montant = fields.Float(
        string="Montant Total (XOF)", compute="_compute_montant", store=True
    )

    etat = fields.Selection([
        ("brouillon", "Brouillon"),
        ("envoye", "Envoyé"),
        ("paye", "Payé"),
    ], default="brouillon", tracking=True)

    notes = fields.Text(string="Notes internes")

    attachment_ids = fields.Many2many(
        "ir.attachment",
        "parc_facture_attachment_rel",
        "facture_id", "attachment_id",
        string="Pièces jointes"
    )

    # -----------------------------------------------------------------
    # Séquence Automatique
    # -----------------------------------------------------------------
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", "Nouveau") == "Nouveau":
                vals["name"] = self.env["ir.sequence"].next_by_code("parc.facture") or "FAC-00000"
        records = super().create(vals_list)
        records._send_invoice_mail()
        return records

    # -----------------------------------------------------------------
    # Calcul du Montant
    # -----------------------------------------------------------------
    @api.depends("contrat_id.montant_ht")
    def _compute_montant(self):
        for rec in self:
            rec.montant = rec.contrat_id.montant_ht if rec.contrat_id else 0.0

    # -----------------------------------------------------------------
    # Envoi de la Facture par E-mail
    # -----------------------------------------------------------------
    def _send_invoice_mail(self):
        for invoice in self:
            template = self.env.ref(
                "parc_facturation.mail_template_facture_parc",
                raise_if_not_found=False
            )
            if template:
                template.send_mail(invoice.id, force_send=True)
                invoice.etat = "envoye"

    # -----------------------------------------------------------------
    # Actions Rapides : Envoyer et Payer
    # -----------------------------------------------------------------
    def action_mark_sent(self):
        self.etat = "envoye"

    def action_register_payment(self):
        self.etat = "paye"

    # -----------------------------------------------------------------
    # Génération PDF de la Facture (Portail)
    # -----------------------------------------------------------------
    def action_download_pdf(self):
        return self.env.ref("parc_facturation.report_facture_portal").report_action(self)
