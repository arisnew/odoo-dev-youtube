# -*- coding: utf-8 -*-
{
    'name': "Arisnew Academy",

    'summary': """
        Academy modul""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Arisnew",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/course_views.xml',
        'views/course_category_views.xml',
        'views/res_partner.xml',

        'views/session_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}