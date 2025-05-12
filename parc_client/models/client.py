# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError


class ClientEntreprise(models.Model):
    _name = "parc.client"
    _description = "Client Entreprise"
    _inherits = {"res.partner": "partner_id"}
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    # ------------------------------------------------------------------ Liens
    partner_id = fields.Many2one("res.partner", required=True, ondelete="cascade")

    # ------------------------------------------------------------------ Spécifiques
    responsable = fields.Char(tracking=True)
    siret = fields.Char(string="SIRET / NIF")
    site_ids = fields.One2many("parc.client.site", "client_id")

    # ------------------------------------------------------------------ Alias éditables
    name = fields.Char(related="partner_id.name", readonly=False, required=True)
    email = fields.Char(related="partner_id.email", readonly=False)
    telephone = fields.Char(
        related="partner_id.phone", readonly=False,
        string="Téléphone (login alternatif)",
    )
    adresse = fields.Char(
        related="partner_id.street", readonly=False,
        string="Adresse postale",
    )

    # ------------------------------------------------------------------ CREATE
    @api.model_create_multi
    def create(self, vals_list):
        """
        1. crée le res.partner si besoin
        2. crée le parc.client
        3. crée (ou synchronise) l'utilisateur portail et envoie le mail de
           définition de mot de passe.
        """
        User = self.env["res.users"].with_user(SUPERUSER_ID)
        portal_group = self.env.ref("base.group_portal")

        # 1) garantir un partner et un login correct
        for vals in vals_list:
            partner = False
            if vals.get("partner_id"):
                partner = self.env["res.partner"].browse(vals["partner_id"])

            partner_name = vals.get("name") or partner and partner.name
            if not partner_name:
                raise ValidationError(_("Le client doit avoir un nom."))

            login = vals.get("email") or vals.get("telephone") \
                    or partner and (partner.email or partner.phone)
            if not login:
                raise ValidationError(
                    _("Le client « %s » doit avoir au moins un e-mail ou un téléphone pour créer le compte portail.") % partner_name
                )

            if not partner:
                partner = self.env["res.partner"].create({
                    "name": partner_name,
                    "email": vals.get("email"),
                    "phone": vals.get("telephone"),
                    "street": vals.get("adresse"),
                    "is_company": True,
                })
                vals["partner_id"] = partner.id

        # 2) création des parc.client
        clients = super().create(vals_list)

        # 3) compte portail + invitation
        for client in clients:
            partner = client.partner_id
            login = partner.email or partner.phone

            user = User.search([("login", "=", login)], limit=1)
            if not user:
                user = User.create({
                    "name": partner.name,
                    "login": login,
                    "partner_id": partner.id,
                    "groups_id": [(6, 0, [portal_group.id])],
                })
            else:
                # s'assurer que le groupe et le partner sont corrects
                if portal_group.id not in user.groups_id.ids:
                    user.groups_id = [(4, portal_group.id)]
                if user.partner_id != partner:
                    user.partner_id = partner

            # envoyer le lien si l'utilisateur n'a pas encore de mot de passe
            if not user.password:
                user.action_reset_password()

        return clients
