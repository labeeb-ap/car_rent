# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CAR RENT',
    'version': '1.4',
    'summary': 'CAR FOR RENT',
    'sequence': 10,

    'depends': ['base_setup','fleet','sale'],
    'data': [
        'views/sale_order_line.xml',
        'views/vehicle_rent.xml',
        'security/ir.model.access.csv'

    ],

    'installable': True,
    'application': True,


    'author': 'labeeb',
    'license': 'LGPL-3',
}
