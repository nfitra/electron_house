from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    is_customer = fields.Boolean(string='Customer', default=False)
    is_employee = fields.Boolean(string='Employee', default=False)
