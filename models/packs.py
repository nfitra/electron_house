from odoo import fields, models, api


class Packs(models.Model):
    _name = 'electron.packs'
    _description = 'Packs'

    name = fields.Char(
        string='Name',
        required=True)

    items_ids = fields.Many2many(
        comodel_name='electron.items',
        string='Items_ids')

    total = fields.Integer(compute='_compute_total', string='Total', store=True)

    @api.depends('items_ids')
    def _compute_total(self):
        for record in self:
            record.total = sum(record.items_ids.mapped('price'))
