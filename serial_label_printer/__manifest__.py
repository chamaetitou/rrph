{
    'name': 'Serial Label Printer',
    'version': '18.0.1.0',
    'summary': 'Generate serial number labels with barcode',
    'description': 'This module allows you to generate serial number labels with barcode through a wizard.',
    'author': 'IDBLAID Nabil',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/serial_label_views.xml',
        'views/wizard_views.xml',
        'reports/serial_label_report.xml',
        'reports/serial_label_template.xml',
        # 'views/ir_sequence_views.xml',
    ],
    'installable': True,
    'application': True, 
}
