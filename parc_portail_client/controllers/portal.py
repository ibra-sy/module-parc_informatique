# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class ParcClientPortal(CustomerPortal):
    """
    Portail client : équipements, contrats, factures, tickets + profil.

    IMPORTANT : on travaille désormais avec le modèle `parc.client`
    (lié à res.partner par partner_id).  Toutes les requêtes filtrent
    donc sur ce client ― pas directement sur le partenaire connecté.
    """

    # ------------------------------------------------------------------ #
    #  Helpers
    # ------------------------------------------------------------------ #
    def _get_client(self):
        """Retourne l’enregistrement parc.client associé au partenaire connecté."""
        return request.env['parc.client'].sudo().search(
            [('partner_id', '=', request.env.user.partner_id.id)], limit=1)

    def _prepare_portal_layout_values(self):
        values = super()._prepare_portal_layout_values()
        client = self._get_client()

        values.update({
            'equipment_count': request.env['parc.equipement'].sudo().search_count(
                [('client_id', '=', client.id)]),
            'contract_count': request.env['parc.contrat'].sudo().search_count(
                [('client_id', '=', client.id)]),
            'ticket_count': request.env['parc.intervention'].sudo().search_count(
                [('client_id', '=', client.id)]),
            'invoice_count': request.env['parc.facture'].sudo().search_count(
                [('client_id', '=', client.id)]),
        })
        return values

    # ------------------------------------------------------------------ #
    #  Home & listing pages
    # ------------------------------------------------------------------ #
    @http.route('/my', type='http', auth='user', website=True)
    def portal_home(self, **kw):
        values = self._prepare_portal_layout_values()
        return request.render('parc_portail_client.portal_my_home', values)

    @http.route('/my/equipments', type='http', auth='user', website=True)
    def portal_equipments(self, **kw):
        client = self._get_client()
        equipements = request.env['parc.equipement'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render('parc_portail_client.portal_my_equipments',
                              {'equipments': equipements})

    @http.route('/my/contracts', type='http', auth='user', website=True)
    def portal_contracts(self, **kw):
        client = self._get_client()
        contrats = request.env['parc.contrat'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render('parc_portail_client.portal_my_contracts',
                              {'contracts': contrats})

    @http.route('/my/invoices', type='http', auth='user', website=True)
    def portal_invoices(self, **kw):
        client = self._get_client()
        factures = request.env['parc.facture'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render('parc_portail_client.portal_my_invoices',
                              {'invoices': factures})

    @http.route('/my/tickets', type='http', auth='user', website=True)
    def portal_tickets(self, **kw):
        client = self._get_client()
        tickets = request.env['parc.intervention'].sudo().search(
            [('client_id', '=', client.id)])
        return request.render('parc_portail_client.portal_my_tickets',
                              {'tickets': tickets})

    # ------------------------------------------------------------------ #
    #  Download facture PDF
    # ------------------------------------------------------------------ #
    @http.route('/my/invoices/<int:facture_id>/pdf', auth='user', website=True)
    def portal_invoice_pdf(self, facture_id):
        facture = request.env['parc.facture'].sudo().browse(facture_id)
        if facture.client_id.partner_id.id != request.env.user.partner_id.id:
            return request.not_found()

        pdf, _ = request.env.ref(
            'parc_portail_client.report_facture_portal')._render_qweb_pdf([facture.id])
        return request.make_response(
            pdf, [('Content-Type', 'application/pdf'),
                  ('Content-Disposition',
                   'attachment; filename="Facture-%s.pdf"' % facture.name)])

    # ------------------------------------------------------------------ #
    #  Création de ticket
    # ------------------------------------------------------------------ #
    @http.route('/my/tickets/new', type='http', auth='user',
                website=True, methods=['GET', 'POST'])
    def portal_ticket_create(self, **post):
        client = self._get_client()
        Equip = request.env['parc.equipement'].sudo()

        if http.request.httprequest.method == 'POST':
            equip_id = int(post.get('equipement_id'))
            desc = post.get('description')
            request.env['parc.intervention'].sudo().create({
                'client_id': client.id,
                'equipement_id': equip_id,
                'description': desc,
                'etat': 'brouillon',
            })
            return request.redirect('/my/tickets')

        equipements = Equip.search([('client_id', '=', client.id)])
        return request.render('parc_portail_client.portal_ticket_new',
                              {'equipments': equipements})

    # ------------------------------------------------------------------ #
    #  Profil client – édition (on continue à modifier res.partner)
    # ------------------------------------------------------------------ #
    @http.route('/my/profile', type='http', auth='user',
                website=True, methods=['GET', 'POST'])
    def portal_profile(self, **post):
        partner = request.env.user.partner_id

        if http.request.httprequest.method == 'POST':
            partner.sudo().write({
                'name':      post.get('name'),
                'email':     post.get('email'),
                'phone':     post.get('phone'),
                'street':    post.get('street'),
                'city':      post.get('city'),
                'zip':       post.get('zip'),
                'country_id': int(post.get('country_id'))
                              if post.get('country_id') else False,
            })
            return request.redirect('/my')

        countries = request.env['res.country'].sudo().search([])
        return request.render('parc_portail_client.portal_my_profile',
                              {'partner': partner, 'countries': countries})
