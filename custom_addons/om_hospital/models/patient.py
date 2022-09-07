from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread','mail.activity.mixin']  #inherit for oe.chatter , mixin is for activity_ids
    
    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string="Active", default="True")