from odoo import fields, models, api


class Customer(models.Model):
    _name = 'electron.customer'
    _description = 'Customer'

    name = fields.Char(
        string='Name', 
        required=True)
    
    age = fields.Integer(
        string='Age', 
        required=False)
    
    address = fields.Char(
        string='Address',
        required=False)