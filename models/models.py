# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class test(models.Model):
#     _name = 'test.test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Test(models.Model):
    _name = 'test.test'

    name = fields.Char(string="Title", required=True)
    purpose = fields.Text()

    tester = fields.Many2one('res.partner', ondelete='set null', string="")
