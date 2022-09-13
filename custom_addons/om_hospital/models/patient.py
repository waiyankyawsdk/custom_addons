from datetime import date
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread','mail.activity.mixin']  #inherit for oe.chatter , mixin is for activity_ids
    
    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute="_compute_age", tracking=True)
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender', tracking=True, default="male")
    active = fields.Boolean(string="Active", default="True")
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            today = date.today()
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year
            else:
                record.age = 0