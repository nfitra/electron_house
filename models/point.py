from odoo import fields, models, api


class Point(models.Model):
    _name = 'electron.point'
    _description = 'Point'

    customer = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True)

    point = fields.Integer(
        string='Point',
        required=True)



