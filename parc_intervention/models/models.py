# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class parc_intervention(models.Model):
#     _name = 'parc_intervention.parc_intervention'
#     _description = 'parc_intervention.parc_intervention'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

