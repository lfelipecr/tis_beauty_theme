# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2021. All rights reserved.

from odoo import fields, models, SUPERUSER_ID, api


class BeautyBanner1(models.Model):
    _name = "beauty.banner1"
    _description = "Beauty Banner"

    name = fields.Char(string="Name")
    header = fields.Char(string="Header")
    description = fields.Char(string="Description")
    image1 = fields.Binary(string="Upload Image")


class BeautyBanner2(models.Model):
    _name = "beauty.banner2"
    _description = "Beauty Banner 2"

    name = fields.Char(string="Name")
    header = fields.Char(string="Header")
    image1 = fields.Binary(string="Upload Image")
    caption = fields.Char(string="Caption")


class BeautyCategory(models.Model):
    _name = "beauty.product.category"
    _rec_name = 'category_id'
    _description = "Category"

    category_id = fields.Many2one('product.public.category', string="Category")
    image = fields.Binary(string='Image', help="Width:377px Height:566px")


class OurProducts(models.Model):
    _name = "our.products"
    _description = "Our Products"

    product_id = fields.Many2one('product.template', string="Product")
    name = fields.Char(string="Name")


class PopularProducts(models.Model):
    _name = "popular.products"
    _description = "Popular Products"

    product_id = fields.Many2one('product.template', string="Product")
    name = fields.Char(string="Name")


class BestSeller(models.Model):
    _name = "best.seller"
    _description = "Best Seller"

    product_id = fields.Many2one('product.template', string="Product")
    name = fields.Char(string="Name")


class Website(models.Model):
    _inherit = 'website'

    def get_main_banner_one(self):
        main_banner = self.env['beauty.banner1'].sudo().search([])
        return main_banner

    def get_full_banner_one(self):
        half_banner = self.env['beauty.banner2'].sudo().search([])
        return half_banner

    def get_beauty_product_category(self):
        beauty_product_category = self.env['beauty.product.category'].sudo().search([])
        return beauty_product_category

    def get_our_products(self):
        our_products = self.env['our.products'].sudo().search([])
        return our_products

    def get_popular_products(self):
        popular_products = self.env['popular.products'].sudo().search([])
        return popular_products

    def get_best_seller(self):
        best_seller = self.env['best.seller'].sudo().search([])
        return best_seller


class IrModuleModule(models.Model):
    _name = "ir.module.module"
    _description = 'Module'
    _inherit = _name

    @api.model
    def _theme_remove(self, website):
        if website.theme_id.name == "tis_beauty_theme":
            header = self.env['ir.ui.view'].sudo().search([('name', '=', 'Website beauty Header')])
            header.unlink()
            footer = self.env['ir.ui.view'].sudo().search([('name', '=', 'beauty Footer')])
            footer.unlink()
            footer_cpy = self.env['ir.ui.view'].sudo().search([('name', '=', 'beauty Copyright')])
            footer_cpy.unlink()
            home = self.env['ir.ui.view'].sudo().search([('name', '=', 'Home beauty')])
            home.unlink()
            env = api.Environment(self.env.cr, SUPERUSER_ID, {})
            default_website = env.ref('website.default_website', raise_if_not_found=False)
            default_homepage = env.ref('website.homepage_page', raise_if_not_found=False)
            default_website.homepage_id = default_homepage.id
        return super(IrModuleModule, self)._theme_remove(website)
