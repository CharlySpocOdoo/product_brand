{
    'name': 'Product Brand',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'Gestión de marcas para productos',
    'description': """
        Este módulo permite:
        - Crear y gestionar marcas de productos
        - Asignar marcas a productos (relación uno a muchos)
        - Campo obligatorio para marca en productos
        - Menú dedicado para gestionar marcas
    """,
    'author': 'Charly boy',
    'website': 'https://www.rosadelima.mx',
    'depends': ['base', 'product', 'sale', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_brand_views.xml',
        'views/product_template_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

