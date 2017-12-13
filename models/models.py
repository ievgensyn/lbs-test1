# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

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

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('test.session', 'test_id', string="Sessions")


class Session(models.Model):
    _name = 'test.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date()
    duration = fields.Float(string="Duration in days", compute='compute_delta')

    #@api.depends('start_date', 'end_date', 'duration')
    def compute_delta(self):
        for i in self:
            start_date = fields.Datetime.from_string(i.start_date)
            end_date = fields.Datetime.from_string(i.end_date)
            i.duration = (end_date - start_date).days


    tester_id = fields.Many2one('res.partner', string="Tester")
    test_id = fields.Many2one('test.test', ondelete='cascade', string="Test", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
