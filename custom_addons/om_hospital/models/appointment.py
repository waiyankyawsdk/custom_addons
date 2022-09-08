from email.policy import default
from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']  
    _description = "Hospital Appointment"

    patient_ids = fields.Many2one(string="Patient", comodel_name="hospital.patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default= fields.Date.context_today)