from odoo import http
from odoo.http import request, content_disposition
from odoo.addons.portal.controllers.portal import CustomerPortal


class ParcClientPortal(CustomerPortal):
    """
    Portail client : équipements, contrats, factures, tickets + profil.
    """

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _get_client(self):
        """Renvoie l’enregistrement parc.client associé au partenaire connecté (ou False)."""
        return request.env['parc.client'].sudo().search(
            [('partner_id', '=', request.env.user.partner_id.id)], limit=1)

    # ------------------------------------------------------------------
    # Layout values (tableau de bord)
    # ------------------------------------------------------------------
    def _prepare_portal_layout_values(self):
        vals = super()._prepare_portal_layout_values()
        client = self._get_client()
        if not client:
            return vals  # rien à afficher si lien manquant

        domain = [('client_id', '=', client.id)]
        vals.update(
            equipment_count=request.env['parc.equipement'].sudo().search_count(domain),
            contract_count=request.env['parc.contrat'].sudo().search_count(domain),
            ticket_count=request.env['parc.intervention'].sudo().search_count(domain),
            invoice_count=request.env['parc.facture'].sudo().search_count(domain),
        )
        return vals

    # ------------------------------------------------------------------
    # Dashboard
    # ------------------------------------------------------------------
    @http.route("/my", auth="user", website=True)
    def portal_home(self, **kw):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')
        return request.render(
            "parc_portail_client.portal_my_home",
            self._prepare_portal_layout_values()
        )

    # ------------------------------------------------------------------
    # Listes
    # ------------------------------------------------------------------
    @http.route("/my/equipments", auth="user", website=True)
    def portal_equipments(self, **kw):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')

        equipments = request.env['parc.equipement'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render("parc_portail_client.portal_my_equipments",
                              {"equipments": equipments})

    @http.route("/my/contracts", auth="user", website=True)
    def portal_contracts(self, **kw):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')

        contracts = request.env['parc.contrat'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render("parc_portail_client.portal_my_contracts",
                              {"contracts": contracts})

    @http.route("/my/invoices", auth="user", website=True)
    def portal_invoices(self, **kw):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')

        invoices = request.env['parc.facture'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render("parc_portail_client.portal_my_invoices",
                              {"invoices": invoices})

    @http.route("/my/tickets", auth="user", website=True)
    def portal_tickets(self, **kw):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')

        tickets = request.env['parc.intervention'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render("parc_portail_client.portal_my_tickets",
                              {"tickets": tickets})

    # ------------------------------------------------------------------
    # Téléchargement PDF facture sécurisé
    # ------------------------------------------------------------------
    @http.route("/my/invoices/<int:facture_id>/pdf", auth="user", website=True)
    def facture_pdf(self, facture_id):
        facture = request.env['parc.facture'].sudo().browse(facture_id)
        if facture.client_id.partner_id != request.env.user.partner_id:
            return request.not_found()

        pdf, _ = request.env.ref("parc_portail_client.report_facture_portal")._render_qweb_pdf([facture.id])
        
        # Réponse PDF avec header correct
        return request.make_response(pdf, headers=[
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', content_disposition(f"Facture-{facture.name}.pdf")),
        ])

    # ------------------------------------------------------------------
    # Nouveau ticket
    # ------------------------------------------------------------------
    @http.route("/my/tickets/new", auth="user", methods=["GET", "POST"], website=True)
    def ticket_new(self, **post):
        client = self._get_client()
        if not client:
            return request.redirect('/web/login')

        if http.request.httprequest.method == "POST":
            request.env['parc.intervention'].sudo().create({
                "client_id": client.id,
                "equipement_id": int(post.get("equipement_id")),
                "description": post.get("description"),
                "etat": "brouillon",
            })
            return request.redirect("/my/tickets")

        equipments = request.env['parc.equipement'].sudo().search([('client_id', '=', client.id)])
        return request.render("parc_portail_client.portal_ticket_new",
                              {"equipments": equipments})

    # ------------------------------------------------------------------
    # Profil
    # ------------------------------------------------------------------
    @http.route("/my/profile", auth="user", methods=["GET", "POST"], website=True)
    def my_profile(self, **post):
        partner = request.env.user.partner_id
        if http.request.httprequest.method == "POST":
            partner.sudo().write({
                "name": post.get("name"),
                "email": post.get("email"),
                "phone": post.get("phone"),
                "street": post.get("street"),
                "city": post.get("city"),
                "zip": post.get("zip"),
                "country_id": int(post.get("country_id")) if post.get("country_id") else False,
            })
            return request.redirect("/my")

        countries = request.env['res.country'].sudo().search([])
        return request.render("parc_portail_client.portal_my_profile",
                              {"partner": partner, "countries": countries})
