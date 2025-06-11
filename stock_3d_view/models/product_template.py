from odoo import fields, models


class ProductTemplate(models.Model):
    """Class for adding 3D property fields to product.template"""
    _inherit = 'product.template'

    length = fields.Float(string="Length (M)",
                          help="Length of the product in meters")
    width = fields.Float(string="Width (M)",
                         help="Width of the product in meters")
    height = fields.Float(string="Height (M)",
                          help="Height of the product in meters")
    pos_x = fields.Float(string="X (in px)",
                         help="Position of the product along X-axis")
    pos_y = fields.Float(string="Y (in px)",
                         help="Position of the product along Y-axis")
    pos_z = fields.Float(string="Z (in px)",
                         help="Position of the product along Z-axis")

    # def action_view_product_3d_button(self):
    #     """
    #     This method is used to handle the view_product_3d_button button action.
    #     ------------------------------------------------
    #     @param self: object pointer.
    #     @return: client action with product id and company id to display.
    #     """
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'open_form_3d_view',
    #         'context': {
    #             'product_id': self.id,
    #             'company_id': self.company_id.id,
    #         }
    #     }