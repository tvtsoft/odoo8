# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) David Arnold (devCO).
# Author        David Arnold (devCO), dar@devco.co
# Co-Authors    Juan Pablo Aries (devCO), jpa@devco.co
#               Hector Ivan Valencia Muñoz (TIX SAS)
#               Nhomar Hernandez (Vauxoo)
#               Humberto Ochoa (Vauxoo)

{
    'name': 'Colombian - Accounting',
    'version': '0.8',
    'category': 'Localization/Account Charts',
    'description': 'Colombian Accounting and Tax Preconfiguration',
    'author': 'David Arnold BA HSG (devCO)',
    'depends': [
        'account',
        'base_vat',
    ],
    'data': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account_chart_template.xml',
        'data/account.tax.template.csv',
        'wizard/account_wizard.xml',
    ],
    'demo': [],
    'installable': False,
}
