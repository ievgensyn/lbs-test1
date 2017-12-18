# -*- coding: utf-8 -*-
{
    'name': "Test",

    'summary': """
        final problemset LBS course""",

    'description': """
        - This module creates main menu 'Test' and two submenus 'Tests' and 'Test session'
        - inherites form view from res.partner, that shows a field 'isTester' (readonly, boolean=True if there is one test with this partner)
        - inherites tree view and search field for res.partner-model with filter for Partners, who has tests in the next 30 days
    """,

    'author': "Ievgen Synchyshyn",
    'website': "http://www.mycompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/lbstest.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}