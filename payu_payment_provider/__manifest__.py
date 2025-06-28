{
    'name': 'Payment Acquirer: MyProvider',
    'version': '1.0',
    'category': 'Accounting/Payment',
    'summary': 'Payment Acquirer for MyProvider',
    'description': """Payment acquirer integration for MyProvider""",
    'depends': ['payment'],
    'data': [
        'views/payment_myprovider_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
