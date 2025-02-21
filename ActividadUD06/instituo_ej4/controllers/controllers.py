# -*- coding: utf-8 -*-
# from odoo import http


# class InstituoEj4(http.Controller):
#     @http.route('/instituo_ej4/instituo_ej4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instituo_ej4/instituo_ej4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('instituo_ej4.listing', {
#             'root': '/instituo_ej4/instituo_ej4',
#             'objects': http.request.env['instituo_ej4.instituo_ej4'].search([]),
#         })

#     @http.route('/instituo_ej4/instituo_ej4/objects/<model("instituo_ej4.instituo_ej4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instituo_ej4.object', {
#             'object': obj
#         })

