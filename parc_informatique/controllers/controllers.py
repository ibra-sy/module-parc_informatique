# -*- coding: utf-8 -*-
# from odoo import http


# class ParcInformatique(http.Controller):
#     @http.route('/parc_informatique/parc_informatique', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_informatique/parc_informatique/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_informatique.listing', {
#             'root': '/parc_informatique/parc_informatique',
#             'objects': http.request.env['parc_informatique.parc_informatique'].search([]),
#         })

#     @http.route('/parc_informatique/parc_informatique/objects/<model("parc_informatique.parc_informatique"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_informatique.object', {
#             'object': obj
#         })

