# -*- coding: utf-8 -*-
# from odoo import http


# class ChenabClubVoucher(http.Controller):
#     @http.route('/chenab_club_voucher/chenab_club_voucher/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chenab_club_voucher/chenab_club_voucher/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chenab_club_voucher.listing', {
#             'root': '/chenab_club_voucher/chenab_club_voucher',
#             'objects': http.request.env['chenab_club_voucher.chenab_club_voucher'].search([]),
#         })

#     @http.route('/chenab_club_voucher/chenab_club_voucher/objects/<model("chenab_club_voucher.chenab_club_voucher"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chenab_club_voucher.object', {
#             'object': obj
#         })
