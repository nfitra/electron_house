from odoo import fields, models, api, _
from odoo.exceptions import UserError

class Order(models.Model):
    _name = 'electron.order'
    _description = 'Order'

    name = fields.Char(
        string='Order Code',
        required=True,
        default='New',
        readonly=True)

    customer = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True)

    point_customer = fields.Integer(
        string='Point Customer',
        required=True)

    @api.onchange('customer')
    def onchange_point_customer(self):
        for record in self:
            record.point_customer = record.env['electron.point'].search([('customer.id','=', record.customer.id)]).point

    date_created = fields.Datetime(
        string='Date Created',
        required=True,
        readonly=True,
        default=fields.datetime.now())

    date_payed = fields.Datetime(
        string='Date Payed',
        required=False,
        readonly=True)

    discount_type = fields.Selection(
        string='Discount Type',
        selection=[('none', 'None'),
                   ('voucher', 'Voucher'),
                   ('point', 'Point'), ],
        required=True,
        default='none')

    voucher_discount = fields.Many2one(
        comodel_name='electron.voucher',
        string='Voucher',
        required=False,
        default=False)

    point_discount = fields.Integer(
        string='Point',
        required=False,
        default=False)

    @api.onchange('discount_type')
    def onchange_discount(self):
        for record in self:
            record.voucher_discount = None
            record.point_discount = None

    items_ids = fields.Many2many(
        comodel_name='electron.items',
        string='Items',)
    
    packs_ids = fields.Many2many(
        comodel_name='electron.packs', 
        string='Packs',)

    total_items = fields.Integer(compute='_compute_total', string='Total Items', store=True)

    @api.depends('items_ids')
    def _compute_total(self):
        for record in self:
            self.total_items = sum(self.items_ids.mapped('price'))

    total_packs = fields.Integer(compute='_compute_total', string='Total Packs', store=True)

    @api.depends('packs_ids')
    def _compute_total(self):
        for record in self:
            self.total_packs = sum(self.packs_ids.mapped('total'))

    total = fields.Integer(
        string='Total Price',
        required=False)

    total_with_disc = fields.Integer(
        string='Total With Discount',
        required=False)

    @api.onchange('items_ids','packs_ids','point_discount','voucher_discount')
    def onchange_total(self):
        _total = 0
        total_all = sum(self.items_ids.mapped('price')) + sum(self.packs_ids.mapped('total'))
        if(self.discount_type == 'voucher'):
            _total = total_all - (total_all * self.voucher_discount.percentage/100)
        elif(self.discount_type == 'point'):
            _total = total_all - self.point_discount
        else:
            _total = total_all

        self.total = total_all
        self.total_with_disc = _total

    state = fields.Selection(
        string='State',
        selection=[('ongoing', 'Ongoing'),
                   ('payed', 'Payed'),
                   ('cancelled', 'Cancelled'),],
        required=True,
        readonly=True,
        default='ongoing')

    notes = fields.Char(
        string='Notes',
        required=False)

    @api.model
    def create(self, vals):
        point = 0

        items = vals.get('items_ids')
        packs = vals.get('packs_ids')
        if (sum(items[0][2]) == 0 and sum(packs[0][2]) == 0):
            raise UserError(_('Must input item to buy or pack to buy'))

        if (vals.get('total_with_disc') < 0):
            raise UserError(_('Total of payment is abnormal'))

        if (vals.get('discount_type') == 'point'):
            point = vals.get('point_customer') - vals.get('point_discount')
            if (point < 0):
                raise UserError(_('Point discount exceeds the point of a customer has'))

            self.env['electron.point'].search([('customer.id', '=', vals.get('customer'))]).write({'point': point})

        vals['name'] = self.env['ir.sequence'].next_by_code('electron.order') or 'New'
        return (super(Order, self).create(vals))

    def action_pay(self):
        for record in self:
            record.state = 'payed'
            record.date_payed = fields.datetime.now()

    def action_reset(self):
        for record in self:
            record.state = 'ongoing'
            record.date_payed = None

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
        return {
            'name': ('Add Reason'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'electron.cancel',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }