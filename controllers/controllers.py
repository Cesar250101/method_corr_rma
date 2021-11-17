# -*- coding: utf-8 -*-
from odoo import http

# class MethodCorrRma(http.Controller):
#     @http.route('/method_corr_rma/method_corr_rma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_corr_rma/method_corr_rma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_corr_rma.listing', {
#             'root': '/method_corr_rma/method_corr_rma',
#             'objects': http.request.env['method_corr_rma.method_corr_rma'].search([]),
#         })

#     @http.route('/method_corr_rma/method_corr_rma/objects/<model("method_corr_rma.method_corr_rma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_corr_rma.object', {
#             'object': obj
#         })