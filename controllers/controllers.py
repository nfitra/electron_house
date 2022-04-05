# -*- coding: utf-8 -*-
# from odoo import http


# class ElectronHouse(http.Controller):
#     @http.route('/electron_house/electron_house/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/electron_house/electron_house/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('electron_house.listing', {
#             'root': '/electron_house/electron_house',
#             'objects': http.request.env['electron_house.electron_house'].search([]),
#         })

#     @http.route('/electron_house/electron_house/objects/<model("electron_house.electron_house"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('electron_house.object', {
#             'object': obj
#         })
