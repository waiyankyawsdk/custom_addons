{
    'name' : 'Travel Manager',
    'version' : '1.1',
    'category' : 'Extra Tools',
    'depends' : ['base', 'mail', 'uom'],
    'description' : """
    """,
    'data' :[
        'security/ir.model.access.csv',
        'views/travel_view.xml',
        'data/travels.xml',
        'report/travel_report.xml'
    ],
    'demo':[

    ],
    'installable':True,
    'licence' : 'LGPL-3'
}
