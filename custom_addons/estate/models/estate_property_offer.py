from odoo import api, fields, models
from datetime import datetime
from nbformat import ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _sql_constraints = [
        ('price', 'CHECK(price > 0)',
         'The price must be strictly positive.')
    ]

    price = fields.Float()
    status = fields.Selection(
        string = 'status',
        copy = False,
        selection=[('accept','Accepted'),('refuse','Refused')]
    )

    partner_id = fields.Many2one('res.partner', required = True)
    property_id = fields.Many2one('estate.property', required = True)

    validity = fields.Integer(compute = "_compute_validity_date", inverse = "_inverse_validity_date", default = 0, string = "Validity (days)", store= True)
    date_deadline = fields.Date(string="Deadline")

    @api.depends("date_deadline")
    def _compute_validity_date(self):
        for record in self:
            if record.date_deadline and record.create_date:
                valid_date = record.date_deadline - record.create_date.date()
                record.validity = valid_date.days
            else:
                record.validity = 7
                
    def _inverse_validity_date(self):
        for record in self:
            if record.date_deadline:
                self.validity = record.validity
            else:
                self.validity = 7

    def action_confirm(self):
        for record in self:
            record.status = "accept"
            # if record.price:               
            #     record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id.name

    def action_cancel(self):
        for record in self:
            record.status = "refuse"

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price and record.price < 0:
                raise ValidationError("The expected price must be strictly positive. %s" % record.price)
    
