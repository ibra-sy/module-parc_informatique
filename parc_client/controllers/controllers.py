# -*- coding: utf-8 -*-
# from odoo import http


# class ParcClient(http.Controller):
#     @http.route('/parc_client/parc_client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_client/parc_client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_client.listing', {
#             'root': '/parc_client/parc_client',
#             'objects': http.request.env['parc_client.parc_client'].search([]),
#         })

#     @http.route('/parc_client/parc_client/objects/<model("parc_client.parc_client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_client.object', {
#             'object': obj
#         })

