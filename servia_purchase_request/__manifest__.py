# -*- coding: utf-8 -*-
{
    'name': 'Servia Purchase Requisition',
    'version': '17.0.1.0.0',
    'category': 'Purchases',
    'summary': 'Raise internal purchase requisitions: item, quantity, needed-by date, department and estimated cost, with a simple approve workflow.',
    'description': """
Servia Purchase Requisition
===========================
A simple purchase requisition & approval register.

* Record each request: item, quantity, department and needed-by date.
* Capture estimated cost, requester and justification.
* Approve requests; filter and group by department or status.
* Simple purchase requisition log before raising a PO.
* Works on Odoo Community, Enterprise and Odoo.sh, versions 12 to 19

Installation and customization by Servia - see the description page.
""",
    'author': 'Servia',
    'website': 'https://servia.ae',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'USD',
    'support': 'support@servia.ae',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/servia_purchase_request_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
