from odoo import api, fields, models

class HospitalOperation(models.Model):
    _name = "hospital.operation"
    _description = "Hospital Operation"
    _log_access = False
    _rec_name = 'operation_name'

    doctor_id = fields.Many2one('res.users', string="Doctor")
    operation_name = fields.Char(string="Name")
    reference_record = fields.Reference(selection=[('hospital.patient', 'Patients'),('hospital.appointment','Appointments')], string="Record")

    @api.model
    def name_create(self, name):
        return self.create({'operation_name':name}).name_get()[0]