# -*- coding: utf-8 -*-
from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model,
    # by default partners are not tester
    isTester = fields.Boolean("isTester", default=False, readonly=True)
    session_ids = fields.Many2many('lbs.test', string="Test")