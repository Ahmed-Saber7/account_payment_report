# -*- coding: utf-8 -*-
{
    'name': "Account Payment Report",

    'summary': """
       Account Payment Report""",

'description': """
        This module allow To Print Report For Payments From Wizard at Specific Date.
    """,
    'author': "Ahmed Saber",
    'category': 'accounting',
    'version': '0.1',
    'depends': ['base','account'],
    'data': [
        # 'security/ir.model.access.csv',
        'report/payment_report_template.xml',
        'report/payment_report_ref.xml',
        'views/views.xml',
    ]

}