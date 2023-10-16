from odoo import models, fields

class Travel(models.Model):
    _name = 'travel.travel'
    _description = "Travel Manager"

    name = fields.Char(string="Name")
    destination = fields.Char(string="Destination")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
