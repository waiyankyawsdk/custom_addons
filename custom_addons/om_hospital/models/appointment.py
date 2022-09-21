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
    
    ref = fields.Char(string="Reference", help="Reference of Patients")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')
    ])
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Canceled')
    ],string="Status", default="draft")
    doctor_id = fields.Many2one(comodel_name="res.users", string="Doctor")
    pharmacy_line_ids = fields.One2many("appointment.pharmacy.lines", "appointment_id" , string="Pharmacy Lines")
    
    @api.onchange('patient_ids')
    def _onchange_patient_id(self):
        self.ref = self.patient_ids.ref
    
    # Action button test
    def action_test(self):
        print("Button Clicked!!!!!!!!!!!!!!!!!!!!!")
        return {
            'effect' :{
                'fadeout' : 'slow',
                'message' : 'Click Successfully',
                'type'    : 'rainbow_man'
        }}
        
    def action_in_consultation(self):
        for record in self:
            record.state = 'in_consultation'
            
    def action_done(self):
        for record in self:
            record.state = 'done'
    
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
    
    def action_draft(self):
        for record in self:
            record.state = 'draft'

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one("product.product")
    price_unit = fields.Float(related="product_id.list_price", string="Price")
    qty = fields.Integer(string="Quantity", default="1")
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
