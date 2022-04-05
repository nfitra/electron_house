from odoo import fields, models, api

class Employee(models.Model):
    _name = 'electron.employee'
    _description = 'Employee'

    name = fields.Char(
        string='Name',
        required=True)

    age = fields.Integer(
        string='Age',
        required=False)

    address = fields.Char(
        string='Address',
        required=False)


