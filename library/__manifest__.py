# -*- coding: utf-8 -*-
{
    'name':        "Library",

    'summary':
                   """
                   library
                   """,

    'description': """
        Manage books, cutomers, authors ...
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'Library',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends':     ['base', 'product'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
        "views/library_view.xml",
        "views/library_menus.xml",
    ],
    # only loaded in demonstration mode
    'demo':        [],
    'license': 'AGPL-3',
}
