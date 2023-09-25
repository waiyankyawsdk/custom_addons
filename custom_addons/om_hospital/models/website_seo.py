from odoo import models, fields

class WebSiteSeo(models.model):
    _name = 'website.seo'
    _inherit = ['website.seo.metadata']
    name = fields.Char('Name', required=True)
    date = fields.Date('Date')

    def _default_website_meta(self):
        res = super(WebSiteSeo, self)._default_website_meta()
        res['default_opengraph']['og:image'] = self.env['website'].image_url(self, 'image')
        res['default_twitter']['twitter:image'] = self.env['website'].image_url(self, 'image')
        return res
