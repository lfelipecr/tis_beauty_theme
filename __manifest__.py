# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

{
    'name': 'Beauty Shop Theme',
    'version': '14.0.0.6',
    'category': 'Theme/Ecommerce',
    'sequence': 1,
    'summary': 'Ecommerce Beauty Shop Theme',
    'description': '''Ecommerce Beauty Shop Theme''',
    'website': 'https://www.technaureus.com/',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'price': 40,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.jpg'],
    'depends': ['website_sale', 'website_sale_wishlist', 'website_mass_mailing'],
    'live_test_url': 'https://themes.technaureus.com/web/database/selector',
    'data': [
        'security/ir.model.access.csv',
        'views/banner_backend_views.xml',
        'views/beauty_category_views.xml',
        'views/beauty_products_views.xml',
        'views/h_f_beauty.xml',
        'views/homepage_beauty.xml'
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
