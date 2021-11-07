from odoo import http
from odoo.http import request


class Contact_Us(http.Controller):

    @http.route('/mcmillanwoods/support', type='http', auth="public")
    def contact(self, **kw):
        request._cr = None
        return request.render("odoo_support.contact_us")
