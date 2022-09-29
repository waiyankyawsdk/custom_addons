import datetime
from odoo import api, fields, models

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one(comodel_name="hospital.appointment",string="Appointment")
    reason = fields.Text()
    date_cancel = fields.Date(string="Cancellation Date")

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['date_cancel'] = datetime.date.today()
        return res
    
    def action_cancel(self):
        return