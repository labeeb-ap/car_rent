from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError




class SaleRentalLine(models.Model):
    _name = 'sale.rental.line'
    _description = 'Vehicle Rental Line'

    order_id = fields.Many2one('sale.order')

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle", required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    pickup_location = fields.Selection([
        ('doha', 'Doha'),
        ('wakra', 'Al Wakra'),
        ('alkhor', 'Al Khor')
    ], string="Pickup Location", required=True)

    rent_price = fields.Float(string="Rent Price", required=True)
    days = fields.Integer(compute="_compute_days")
    subtotal = fields.Float(compute="_compute_total")

    @api.depends('start_date','end_date')
    def _compute_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                rec.days = (rec.end_date - rec.start_date).days + 1
            else:
                rec.days = 0

    @api.depends('days','rent_price')
    def _compute_total(self):
        for rec in self:
            rec.subtotal = rec.days * rec.rent_price



    @api.constrains('start_date','end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date:
                if rec.end_date < rec.start_date:
                    raise ValidationError("End date must be after start date.")











class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rental_line_ids = fields.One2many(
        'sale.rental.line',
        'order_id',
        string="Vehicle Rental Lines"
    )

    rental_total = fields.Float(
        string="Rental Total",
        compute="_compute_rental_total",
        store=True
    )

    @api.depends('rental_line_ids.subtotal')
    def _compute_rental_total(self):
        for order in self:
            order.rental_total = sum(order.rental_line_ids.mapped('subtotal'))
