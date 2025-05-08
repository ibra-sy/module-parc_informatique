# -*- coding: utf-8 -*-
# from odoo import http


# class ParcIntervention(http.Controller):
#     @http.route('/parc_intervention/parc_intervention', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_intervention/parc_intervention/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_intervention.listing', {
#             'root': '/parc_intervention/parc_intervention',
#             'objects': http.request.env['parc_intervention.parc_intervention'].search([]),
#         })

#     @http.route('/parc_intervention/parc_intervention/objects/<model("parc_intervention.parc_intervention"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_intervention.object', {
#             'object': obj
#         })

