from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(
        'product.brand',
        string='Marca del Producto',
        required=False,
        help='Marca a la que pertenece este producto',
        ondelete='restrict'
    )
