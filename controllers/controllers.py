# -*- coding: utf-8 -*-
from odoo import http

# class TdsiModel(http.Controller):
#     @http.route('/tdsimodel/tdsimodel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdsimodel/tdsimodel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdsimodel.listing', {
#             'root': '/tdsimodel/tdsimodel',
#             'objects': http.request.env['tdsimodel.tdsimodel'].search([]),
#         })

#     @http.route('/tdsimodel/tdsimodel/objects/<model("tdsimodel.tdsimodel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdsimodel.object', {
#             'object': obj
#         })
