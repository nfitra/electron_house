from odoo import api, fields, models


class Items(models.Model):
    _name = 'electron.items'
    _description = 'All Items'

    name = fields.Char(
        string='Name',
        required=True)

    qty = fields.Integer(
        string='Quantity',
        required=True)

    type = fields.Selection(
        string='Type',
        selection=[('entertainments', 'Entertainments'),
                   ('furnitures', 'Furnitures'),
                   ('tools', 'Tools'),
                   ('accessories', 'Accessories'), ],
        required=True)

    price = fields.Integer(
        string='Price',
        required=True)