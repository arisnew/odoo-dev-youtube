# -*- coding: utf-8 -*-
from odoo import http

# class ArisnewAcademy(http.Controller):
#     @http.route('/arisnew_academy/arisnew_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arisnew_academy/arisnew_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arisnew_academy.listing', {
#             'root': '/arisnew_academy/arisnew_academy',
#             'objects': http.request.env['arisnew_academy.arisnew_academy'].search([]),
#         })

#     @http.route('/arisnew_academy/arisnew_academy/objects/<model("arisnew_academy.arisnew_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arisnew_academy.object', {
#             'object': obj
#         })