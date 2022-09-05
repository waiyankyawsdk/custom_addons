# -*- coding: utf-8 -*-
{
    'name' : 'Real Estate',
    'version': '1.0.0',
    'category': 'Estate Property',
    'summary': 'Real Estate Property System',
    'description': """Real Estate Property System""",
    'sequence': -101,
    'depends' : [
        'base'
    ],
    'data' : [        
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',      
        'views/estate_menus.xml',        
        'security/ir.model.access.csv'
        
    ],
    'application' : True,
    'author' : 'Wai Yan Kyaw'
}