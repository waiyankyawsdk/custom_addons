# pylint: disable=C0325
# C0325: Unnecessary parens after 'raise' keyword (superfluous-parens)

import json
from typing import Tuple

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ReportQuery(models.Model):
    NAME = "report.query"
    _name = NAME
    _description = "Report Query"

    name = fields.Char(unique=True, index=True)
    headers = fields.Text()
    headers_list = fields.Text(compute='_compute_headers_list')
    query = fields.Text()

    @classmethod
    def string_to_list(cls, input_str: str)->list:
        return [ x.strip() for x in input_str.split(',') ]

    @api.depends('headers')
    def _compute_headers_list(self):
        for record in self:
            if record.headers:
                record.headers_list = json.dumps(self.string_to_list(record.headers))
            else:
                record.headers_list = "[]"

    def get_headers_list(self) -> list:
        return json.loads(self.headers_list)

    def get_report_info(self, rep_model_name: str) -> Tuple[str, list]:

        report = self.search([('name','=',rep_model_name)])
        # pylint: disable=C0325
        # C0325: Unnecessary parens after 'raise' keyword (superfluous-parens)
        if not report:
            raise(_(ValidationError('Report configuration is needed.')))

        return (report.query, report.get_headers_list())
