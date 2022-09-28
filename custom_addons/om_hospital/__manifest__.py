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
        'mail','product'
        ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
    'application' : True,
}
