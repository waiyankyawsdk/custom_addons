from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _inherit = ['mail.thread','mail.activity.mixin']  #inherit for oe.chatter , mixin is for activity_ids
    
    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute="_compute_age", inverse="_inverse_compute_age", search="_search_age", tracking=True)
    ref = fields.Char(string="Reference")
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender', tracking=True, default="male")
    active = fields.Boolean(string="Active", default="True")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")    
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")
    appointment_count = fields.Integer(compute="_compute_appointment_count", store=True)
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")
    parent = fields.Char()
    martial_status = fields.Selection([('single','Single'),('married','Married')], string="Martial Status", tracking=True)
    partner_name = fields.Char()
    is_birthday = fields.Boolean(string="Birthday?", compute="_compute_is_birthday")
    
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth > fields.Date.today():
                raise ValidationError(_('The entered date cannot be greater than Today!'))
    
    @api.depends('age')
    def _inverse_compute_age(self):
        today = date.today()
        for rec in self:
            rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)
    
    def _search_age(self, operator, value):
        date_of_birth = date.today() - relativedelta.relativedelta(years=value)
        start_of_year = date_of_birth.replace(day=1, month=1)
        end_of_year = date_of_birth.replace(day=31, month=12)
        return [('date_of_birth','>=', start_of_year),('date_of_birth','<=', end_of_year)]
        
    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
            
    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_ids:
                raise ValidationError(_("You can't delete a patient with appointments!"))
                
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super().create(vals)
    
    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super().write(vals)
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            today = date.today()
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year
            else:
                record.age = 1
    
    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
    
    @api.depends('date_of_birth')
    def _compute_is_birthday(self):
        for rec in self:
            is_birthday = False
            if rec.date_of_birth:
                today = date.today()
                if today.day == rec.date_of_birth.day and today.month == rec.date_of_birth.month:
                    is_birthday = True
            rec.is_birthday = is_birthday