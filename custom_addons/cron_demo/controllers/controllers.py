# -*- coding: utf-8 -*-
# from odoo import http


# class CronDemo(http.Controller):
#     @http.route('/cron_demo/cron_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cron_demo/cron_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cron_demo.listing', {
#             'root': '/cron_demo/cron_demo',
#             'objects': http.request.env['cron_demo.cron_demo'].search([]),
#         })

#     @http.route('/cron_demo/cron_demo/objects/<model("cron_demo.cron_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cron_demo.object', {
#             'object': obj
#         })
