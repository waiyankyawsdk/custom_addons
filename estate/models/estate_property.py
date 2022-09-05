from nbformat import ValidationError
from numpy import require
from traitlets import default
from odoo import api, fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    _sql_constraints = [
        ('expected_price', 'CHECK(expected_price > 0)',
         'The expected price must be strictly positive.')
    ]

    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy = False, default = lambda x: fields.Date.today())
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(readonly = True, copy = False)
    bedroom = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'orientation',
        selection = [('north','North'), ('south','South'), ('east','East'), ('west','West')],
        help = "Orientation for four directions"
    )
    active = fields.Boolean(active = False)

    #selection default
    state = fields.Selection(
        string = 'state',
        required = True,
        copy = False,
        selection=[('new','New'),('received','Offer Received'),('accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled'),('east','East')],
        help="Orientation for four directions",
        default='new'
    )

    #estate.property.type (many2one)
    property_id = fields.Many2one("estate.property.type",string = "Property Type")
    buyer = fields.Char(copy = False, index=True, tracking=True)
    #defaul user : current user
    seller = fields.Many2one("res.users", string="Salesperson", index=True, tracking=True, default=lambda self: self.env.user)

    #estate.property.tag
    tag_ids = fields.Many2many("estate.property.tag")

    #estate.property.offer (one2many is virtual)
    offer_ids = fields.One2many("estate.property.offer", "property_id")
    #compute attribute
    total_area = fields.Float(compute="_compute_total_area")

    best_price = fields.Float(compute="_compute_best_price", string = "Best Offer")

    @api.depends("living_area" , "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    #max price with mapped()
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            best_price = max(record.offer_ids.mapped('price'))
            record.best_price =  best_price

    #garden onchange
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
            return {'warning': {
                'title': "Warning",
                'message': 'Garden area is set to 10 and orientation is to North'}}
    
    @api.onchange("selling_price")
    def _onchange_selling_price(self):
        for record in self:
            if record.selling_price:
                self._check_expected_price(record)
            else:
                record.selling_price = 0

    def action_sold_property(self):
        for record in self:
            if record.state and record.state != 'canceled':
                record.state = 'sold'
            else:
                return {'warning': {
                        'title': "Warning",
                        'message': 'Canceled property cannot be sold'}}

    def action_cancel_property(self):
         for record in self:
            if record.state and record.state != 'sold':
                record.state = 'canceled'
            else:
                return {'warning': {
                        'title': "Warning",
                        'message': 'Sold property cannot be canceled'}}

    @api.constrains('expected_price')
    def _check_expected_price(self):
        for record in self:
            if record.expected_price < 0:
                raise ValidationError("The expected price must be strictly positive. %s" % record.expected_price)
                
    
