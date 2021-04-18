# -*- coding: utf-8 -*-
{
    'name': "Garaje",

    'summary': "Control de Garaje",

    'description': """
        Modulo para el control de Garaje
    """,

    'author': "Cristián R. Olmos - HC Sinergia S.A.",
    'website': "http://www.hcsinergia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 
        #'contacts'
    ],

    # always loaded
    'data': [ 
    #    'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    #indicamos que es una app
    'application': True,
}
