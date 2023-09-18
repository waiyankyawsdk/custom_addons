# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'author': "Wai Yan Kyaw",
    'sequence': -100,
    'depends': [
        'mail','product','board'
        ],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'data/mail_template_data.xml',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/operation_view.xml',
        'views/res_config_settings_views.xml',
        'views/hospital_dashboard.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
    'application' : True,
    'post_init_hook' : 'post_init_hook',
    'post_load' : 'post_load',
}
