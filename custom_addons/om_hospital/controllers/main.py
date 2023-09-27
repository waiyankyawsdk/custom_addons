import xmlrpc.client

from odoo import http
from odoo.http import request

url = 'http://localhost:8016' # odoo instance url
database = 'rd_demo' # database name
user = 'admin' # username
password = '23d4be648a1ec993758b5e0075a94f191f120f86' #api key
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(database, user, password, {})

#access data from odoo or create data in odoo. execute_kw method
model = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

partners_ids = model.execute_kw(database, uid, password, 'res.users', 'search', [])
print(partners_ids)

class SurveyFormController(http.Controller):
    @http.route(['/survey_form'], type='http', auth="user", website=True)
    def survey_form_view(self, **post):
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        if name and email and phone:
            request.env['survey.form'].sudo().create({
                'name': name,
                'email': email,
                'phone': phone,
                'dob': post.get('dob'),
                'qualification': post.get('qualification')
            })
            return request.redirect('/survey_form?submitted=1')
        return request.render('om_hospital.survey_form_template',
                              {'submitted': post.get('submitted', False)})

    @http.route(['/repair_webform'], type='http', auth="public", website=True)
    def repair_webform(self, **kw):
        product_rec = request.env['product.product'].sudo().search([])
        uom = request.env['uom.uom'].sudo().search([])
        customer_id = request.env['res.partner'].sudo().search([])
        location_id = request.env['stock.location'].sudo().search([])
        return request.render("om_hospital.create_repair", {
            'product_rec': product_rec,
            'uom': uom,
            'customer_id': customer_id,
            'location_id': location_id,
            })

    @http.route(['/create/webrepair'], type='http', auth="public", website=True)
    def create_webrepair(self, **kw):
        res = request.env['repair.order'].sudo().create(kw)
        if res:
            return request.redirect('/repair_webform?submitted=1')
        return request.render('om_hospital.repair_webform',
                              {'submitted': kw.get('submitted', False)})

    @http.route('/test/rpc', type='json', auth="none")
    def rpc_route(self, **post):
        pass
