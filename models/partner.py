from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # add a new column to the res.partner model
    tester = fields.Boolean("Tester", default=False)
    session_ids = fields.Many2many('test.session', string="Attended Sesions", readonly=True)
