# -*- coding: utf-8 -*-
# from odoo import http


# class ParcContrat(http.Controller):
#     @http.route('/parc_contrat/parc_contrat', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_contrat/parc_contrat/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_contrat.listing', {
#             'root': '/parc_contrat/parc_contrat',
#             'objects': http.request.env['parc_contrat.parc_contrat'].search([]),
#         })

#     @http.route('/parc_contrat/parc_contrat/objects/<model("parc_contrat.parc_contrat"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_contrat.object', {
#             'object': obj
#         })

