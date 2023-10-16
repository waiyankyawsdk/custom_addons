from odoo import models, fields

from ....enums.patient_enums import GenderTypes, MartialStatus

REPORT_MODEL = 'om_hospital.patient_report_csv_report'

class PatientReportWizard(models.TransientModel):
    NAME = "om_hospital.report.patient"
    _name = NAME

    _description = "Wizard for Patient Report"

    gender_type = fields.Selection(string="Gender", selection=GenderTypes.get_selection_gender_type())
    martial_status = fields.Selection(string="Martial Status", selection=MartialStatus.get_martial_status())

    def print_csv_report(self) -> any:
        gender = GenderTypes.get_label_for_type(self.gender_type)
        martial = MartialStatus.get_label_for_type(self.martial_status)
        return self.env.ref(REPORT_MODEL).report_action(self, data ={'gender_type': self.gender_type, 'martial_status': self.martial_status},
                                                        desc=f"Patient Report : for {martial} {gender}")
