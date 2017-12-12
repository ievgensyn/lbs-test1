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

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('test.session', 'test_id', string="Sessions")


class Session(models.Model):
    _name = 'test.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Integer(string="Duration in days")

    tester_id = fields.Many2one('res.partner', string="Tester")
    test_id = fields.Many2one('test.test', ondelete='cascade', string="Test", required=True)
