import csv
from datetime import date
from enum import IntEnum
import logging
from typing import List
from odoo import models, api, registry
from odoo.tools.misc import get_lang

_logger = logging.getLogger(__name__)

try:
    from ..wizard.patient_report_wizard import PatientReportWizard
    from ....models.report_query import ReportQuery
except ImportError as imp_err:
    _logger.error(imp_err)

class PatientEnum(IntEnum):
    ref = 0
    pname = 1
    gender =2
    martial_status = 3
    partner_name = 4
    phone = 5
    email = 6
    appointment_count = 7
    tags = 8

class PaymentReport(models.AbstractModel):
    NAME = 'report.om_hospital.patient_report_csv_report'
    _name = NAME

    _inherit = 'report.report_csv.abstract'
    _description = 'Patient Report'

    def format_date(self, given_date:date) -> str:
        return given_date.strftime(get_lang(self.env).date_format)

    def execute_query(self, query):
            self.env.cr.execute(query)
            return self.env.cr.fetchall() or False

    def generate_csv_report(self, writer:csv, data:any, report_param:PatientReportWizard)-> None:
        _ = report_param
        query, headers = self.env[ReportQuery.NAME].get_report_info(self._name)
        header_dict = {}
        for enum_value in PatientEnum:
            header_dict[enum_value.name] = headers[enum_value.value]
        writer.writerow(header_dict)
        try:
            patients = self.execute_query(query=self._get_patient_data(query=query, wizard=data))
            if patients:
                for patient in patients:
                    writer.writerow({
                        'ref':patient[PatientEnum.ref.value],
                        'pname':patient[PatientEnum.pname.value],
                        'gender':patient[PatientEnum.gender.value],
                        'martial_status':patient[PatientEnum.martial_status.value],
                        'partner_name':patient[PatientEnum.partner_name.value],
                        'phone':patient[PatientEnum.phone.value],
                        'email':patient[PatientEnum.email.value],
                        'appointment_count':patient[PatientEnum.appointment_count.value],
                        'tags':patient[PatientEnum.tags.value]
                    })
        except csv.Error as err_msg:
            writer.writerow([str(err_msg)])
            raise err_msg

    @classmethod
    def _get_patient_data(cls, query, wizard) -> str:
        wizard_filter = ""
        if 'gender_type' in wizard:
            if wizard['gender_type'] != False:
                wizard_filter += f" WHERE gender = '{wizard['gender_type']}'"
        if 'martial_status' in wizard and 'gender_type' in wizard:
            if wizard['gender_type'] == False and wizard['martial_status'] != False:
                wizard_filter += f" WHERE martial_status = '{wizard['martial_status']}'"
            if wizard['gender_type'] != False and wizard['martial_status'] != False:
                wizard_filter += f" AND martial_status = '{wizard['martial_status']}'"

        query += wizard_filter
        return query

    def csv_report_options(self):
        res = super().csv_report_options()
        res['fieldnames'] +=['ref' ,'pname' ,'gender' ,'martial_status' ,'partner_name' ,'phone' ,'email' ,'appointment_count','tags']
        res['delimiter'] = ','
        res['quoting'] = csv.QUOTE_ALL
        return res
