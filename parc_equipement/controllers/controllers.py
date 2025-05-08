# -*- coding: utf-8 -*-
# from odoo import http


# class ParcEquipement(http.Controller):
#     @http.route('/parc_equipement/parc_equipement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_equipement/parc_equipement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_equipement.listing', {
#             'root': '/parc_equipement/parc_equipement',
#             'objects': http.request.env['parc_equipement.parc_equipement'].search([]),
#         })

#     @http.route('/parc_equipement/parc_equipement/objects/<model("parc_equipement.parc_equipement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_equipement.object', {
#             'object': obj
#         })

