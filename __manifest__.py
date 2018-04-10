# -*- coding: utf-8 -*-
{
    'name': "MODULE_CLASSE_DK",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "teamDSI",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/helico/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/iut_agenda_views.xml',
        'views/iut_classe_views.xml',
        'views/iut_cours_views.xml',
        'views/iut_eleve_views.xml',
        'views/iut_professeur_views.xml',
        'security/tdsimodel_security.xml',
        'datas/datas.xml',
        'views/views.xml',
        'tdsimodel_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
