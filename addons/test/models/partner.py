# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model,
    # by default partners are not tester
    isTester = fields.Boolean("isTester", default=False, readonly=True)
    session_ids = fields.Many2many('lbs.test', ondelete='cascade', string="Test")


class PartnerViews(models.Model):
    _inherit = 'res.partner'

# the idea was to create a model, inherited from res.partner
# using 'domain' in a field. in which to select the session's 'start_date'
# as computed variable that gets all records in test session's partner
# for next 30 days... + define this in partner.xml

