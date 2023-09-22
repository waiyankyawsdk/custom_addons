from odoo import fields, models

class SurveyForm(models.Model):
    _name = 'survey.form'
    name = fields.Char('Title', required=True)
    email = fields.Char('Email', required=True)
    phone = fields.Char('Phone', required=True)
    dob = fields.Date('Release Date')
    qualification = fields.Char('Qualification')
