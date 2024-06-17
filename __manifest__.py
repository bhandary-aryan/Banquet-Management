{
    'name': 'Banquet Management',
    'version': '1.0',
    'category': 'Custom',
    'sequence': -100,
    'summary': 'Module to manage banquets',
    'author': 'Aryan',
    'depends': [
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/report.xml',
        'views/banquet_menu.xml',
        'views/banquet_views.xml',
        'report/report.xml',
        'report/banquet_report.xml',

    ],
    'installable': True,
    'application': True,
}
