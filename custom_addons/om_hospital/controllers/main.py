from odoo import http
from odoo.http import request

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
