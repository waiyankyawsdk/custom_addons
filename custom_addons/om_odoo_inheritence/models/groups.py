from odoo import api, fields, models

class ResGroups(models.Model):
    _inherit = "res.groups" 
        
    #Super function and added user id 
    def get_application_groups(self, domain):
        b2c = self.env.ref('account.group_show_line_subtotals_tax_included').id
        b2b = self.env.ref('account.group_show_line_subtotals_tax_excluded').id
        return super(ResGroups, self).get_application_groups(domain + [('id', 'not in', (b2c, b2b))])