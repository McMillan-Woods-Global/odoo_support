# -*- coding: utf-8 -*-


{
    'name': 'Odoo Software Support',
    'version': '14.0.1.0.0',
    'sequence': -102,
    'summary': """Customized Login page""",
    'description': """"Hyper link and Odoo Support
    """,
    'category': 'Login',
    'author': 'Sarathvc/Jishnukm/McMWG',
    'company': 'McMillan Woods Global',
    'website': "http://www.mcmillanwoods.com/",
    'depends': ['base', 'web'],
    'data': ['views/odoo_support.xml',
             'views/contact.xml'],
    'qweb': [],
    'images': ['static/description/sample.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
