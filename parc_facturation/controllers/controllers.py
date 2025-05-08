# -*- coding: utf-8 -*-
# from odoo import http


# class ParcFacturation(http.Controller):
#     @http.route('/parc_facturation/parc_facturation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_facturation/parc_facturation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_facturation.listing', {
#             'root': '/parc_facturation/parc_facturation',
#             'objects': http.request.env['parc_facturation.parc_facturation'].search([]),
#         })

#     @http.route('/parc_facturation/parc_facturation/objects/<model("parc_facturation.parc_facturation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_facturation.object', {
#             'object': obj
#         })

