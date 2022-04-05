# -*- coding: utf-8 -*-
{
    'name': "electron_house",

    'summary': """
        Electron House sells modern technology stuff for housing""",

    'description': """
        Electron House
    """,

    'author': "Nanda Fitra Tsalatsa",
    'website': "http://www.hashmicro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/items.xml',
        'views/packs.xml',
        'views/voucher.xml',
        'views/point.xml',
        'views/partner.xml',
        'views/order.xml',
        'data/seq_order.xml',
        'report/report.xml',
        'report/report_order.xml',
        'wizard/cancel_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
