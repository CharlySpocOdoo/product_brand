from odoo import models, fields, api


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Marca de Producto'
    _order = 'name'

    name = fields.Char(
        string='Nombre de la Marca',
        required=True,
        translate=True,
        help='Nombre de la marca del producto'
    )
    
    description = fields.Text(
        string='Descripción',
        help='Descripción adicional de la marca'
    )
    
    active = fields.Boolean(
        string='Activo',
        default=True,
        help='Si está desactivado, la marca no será visible en las selecciones'
    )
    
    product_count = fields.Integer(
        string='Número de Productos',
        compute='_compute_product_count',
        help='Número de productos asociados a esta marca'
    )
    
    # Campo para logo de la marca (opcional)
    logo = fields.Image(
        string='Logo de la Marca',
        help='Logo o imagen de la marca'
    )

    @api.depends('name')
    def _compute_product_count(self):
        """Calcula el número de productos por marca"""
        for brand in self:
            brand.product_count = self.env['product.template'].search_count([
                ('brand_id', '=', brand.id)
            ])

    def action_view_products(self):
        """Acción para ver los productos de esta marca"""
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('product.product_template_action')
        action['domain'] = [('brand_id', '=', self.id)]
        action['context'] = {'default_brand_id': self.id}
        return action

    @api.model
    def name_create(self, name):
        """Permite crear marcas rápidamente desde el campo many2one"""
        brand = self.create({'name': name})
        return brand.name_get()[0]
