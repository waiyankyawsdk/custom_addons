from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    color = fields.Integer(string="Color")
