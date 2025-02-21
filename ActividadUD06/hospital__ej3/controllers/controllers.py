# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalEj3(http.Controller):
#     @http.route('/hospital__ej3/hospital__ej3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital__ej3/hospital__ej3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital__ej3.listing', {
#             'root': '/hospital__ej3/hospital__ej3',
#             'objects': http.request.env['hospital__ej3.hospital__ej3'].search([]),
#         })

#     @http.route('/hospital__ej3/hospital__ej3/objects/<model("hospital__ej3.hospital__ej3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital__ej3.object', {
#             'object': obj
#         })

