# -*- coding: utf-8 -*-
{
    'name': "test_module",

    'summary': """
        Sample module    
    """,

    'description': """
        Sample module to illustrate deinstall issues
    """,

    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],
}
