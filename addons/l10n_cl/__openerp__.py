# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Cubic ERP - Teradata SAC. (http://cubicerp.com).

{
    'name': 'Chile Localization Chart Account',
    'version': '1.0',
    'description': """
Chilean accounting chart and tax localization.
==============================================
Plan contable chileno e impuestos de acuerdo a disposiciones vigentes

    """,
    'author': 'Cubic ERP',
    'website': 'http://cubicERP.com',
    'category': 'Localization/Account Charts',
    'depends': [],
    'data': [
        'l10n_cl_chart.xml',
        'account_tax.xml',
        'l10n_cl_wizard.xml',
    ],
    'demo': [],
    'active': False,
    'installable': False,
}
