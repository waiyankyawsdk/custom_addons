from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']  
    _description = "Hospital Appointment"

    patient_ids = fields.Many2one(string="Patient", comodel_name="hospital.patient")
