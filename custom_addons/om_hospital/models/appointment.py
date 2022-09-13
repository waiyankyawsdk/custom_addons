from email.policy import default
from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']  
    _description = "Hospital Appointment"
    _rec_name = "ref"
    patient_ids = fields.Many2one(string="Patient", comodel_name="hospital.patient", tracking=True)
    gender = fields.Selection(related="patient_ids.gender", readonly=False, tracking=True)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now, tracking=True)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today, tracking=True)
    
    ref = fields.Char(string="Reference")

    @api.onchange('patient_ids')
    def _onchange_patient_id(self):
        self.ref = self.patient_ids.ref