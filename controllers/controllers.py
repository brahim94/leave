# -*- coding: utf-8 -*-
# from odoo import http


# class TechLeave(http.Controller):
#     @http.route('/tech_leave/tech_leave/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_leave/tech_leave/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_leave.listing', {
#             'root': '/tech_leave/tech_leave',
#             'objects': http.request.env['tech_leave.tech_leave'].search([]),
#         })

#     @http.route('/tech_leave/tech_leave/objects/<model("tech_leave.tech_leave"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_leave.object', {
#             'object': obj
#         })
