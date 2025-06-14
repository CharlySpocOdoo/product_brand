from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(
        'product.brand',
        string='Marca del Producto',
        required=True,
        help='Marca a la que pertenece este producto',
        ondelete='restrict'
    )

    @api.constrains('brand_id')
    def _check_brand_id(self):
        """Validación para asegurar que la marca sea obligatoria"""
        for product in self:
            if not product.brand_id:
                raise ValidationError("Necesitas ingresar la marca del producto.")

    @api.model
    def create(self, vals):
        """Override del método create para validar marca obligatoria"""
        if not vals.get('brand_id'):
            raise ValidationError("Necesitas ingresar la marca del producto.")
        return super(ProductTemplate, self).create(vals)

    def write(self, vals):
        """Override del método write para validar marca obligatoria"""
        if 'brand_id' in vals and not vals['brand_id']:
            raise ValidationError("Necesitas ingresar la marca del producto.")
        return super(ProductTemplate, self).write(vals)
