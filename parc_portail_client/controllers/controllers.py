# -*- coding: utf-8 -*-
# from odoo import http


# class ParcPortailClient(http.Controller):
#     @http.route('/parc_portail_client/parc_portail_client', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_portail_client/parc_portail_client/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_portail_client.listing', {
#             'root': '/parc_portail_client/parc_portail_client',
#             'objects': http.request.env['parc_portail_client.parc_portail_client'].search([]),
#         })

#     @http.route('/parc_portail_client/parc_portail_client/objects/<model("parc_portail_client.parc_portail_client"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_portail_client.object', {
#             'object': obj
#         })

