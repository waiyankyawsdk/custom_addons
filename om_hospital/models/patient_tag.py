from datetime import date
from odoo import api, fields, models, _

class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True, copy=False)
    color = fields.Integer()
    color_2 = fields.Char()
    sequence = fields.Integer()

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name, active)', 'A tag must be unique!'),
        ('sequece_check', 'CHECK(sequence >0)', 'Sequence must be positive and not zero!'),
    ]
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
            default['sequence'] = 10
        return super().copy(default)
