# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

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
    _name = 'lbs.test'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class Session(models.Model):
    _name = 'lbs.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Float(help="Duration in days", digits=(6, 2))
