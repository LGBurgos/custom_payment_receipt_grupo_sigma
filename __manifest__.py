
{
    'name': 'Custom Payment Method Report',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Customizes the payment method display on payment receipts.',
    'description': """
        This module customizes the payment receipt report to display the payment method name
        instead of its ID, focusing on the payment_method_line_id field.
    """,
    'author': 'Your Name',
    'depends': ['account'],
    'data': [
        'views/report_payment_receipt.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
