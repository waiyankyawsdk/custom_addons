from datetime import date
from odoo import api, fields, models

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    color = fields.Integer()
    color_2 = fields.Char()
    sequence = fields.Integer()

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name, active)', 'A tag must be unique!'),
        ('sequece_check', 'CHECK(sequence >0)', 'Sequence must be positive and not zero!'),
    ]