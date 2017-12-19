# -*- coding: utf-8 -*-

from datetime import timedelta
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

# model test
class Test(models.Model):
    _name = 'lbs.test'

    name = fields.Char(string="Title", required=True)
    purpose = fields.Text()
    tester = fields.Many2one('res.partner', ondelete='set null', string="Tester", domain=[('istester', '=', True)])

    # Add a duplicate option
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Test, self).copy(default)

    # Add SQL constraints
    _sql_constraints = [
        ('name_purpose_check',
         'CHECK(name != purpose)',
         "The title of the test should not be the purpose"),

        ('name_unique',
         'UNIQUE(name)',
         "The test title must be unique"),
    ]


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
            r.duration = (end_date - start_date).days
