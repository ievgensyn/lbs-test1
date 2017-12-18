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

# model test
class Test(models.Model):
    _name = 'lbs.test'

    name = fields.Char(string="Title", required=True)
    purpose = fields.Text()
    tester = fields.Many2one('res.partner', ondelete='set null', string="Tester")


# model test session:
class Session(models.Model):
    _name = 'lbs.session'

    test = fields.Many2one('lbs.test', ondelete='set null', string="Test")
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    duration = fields.Char(help="Duration in day", compute='_compute_duration')

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for r in self:
            if not (r.start_date and r.end_date):
                r.duration = r.duration
                continue
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date)

