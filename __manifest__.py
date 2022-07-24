# -*- coding: utf-8 -*-
{
    'name': "Odoo Document Migration",

    'summary': """
        Migrate Documents from your legacy system/ file system to your Odoo databse """,

    'description': """
        The is app will enable you to migrate Documents from your filesystem to odoo binary fields
    """,

    'author': "Ohia George - ohiageorge@gmail.com (Bitlect Technology)",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 
        'inseta_skills'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/document_migrate_wizard_views.xml',
    ],
}
