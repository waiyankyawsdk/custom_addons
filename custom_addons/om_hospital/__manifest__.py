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
        'mail','product','board', 'contacts'
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
        'views/res_partner_view.xml',
        # 'views/hospital_dashboard.xml',
        'views/survey_form_view.xml',
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
    'assets': {
        'web.assets_backend': [
            'om_hospital/static/src/js/top_bar.js',
            'om_hospital/static/src/js/res_partner.js',
            'om_hospital/static/src/scss/style.scss'
        ],
        'web.assets_qweb': [
            'om_hospital/static/src/xml/partner_templates.xml',
        ]
    },
}
