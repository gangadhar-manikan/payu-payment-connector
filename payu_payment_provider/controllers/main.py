from odoo import http
from odoo.http import request

class MyProviderController(http.Controller):

    @http.route('/payment/myprovider/return', type='http', auth='public', methods=['GET', 'POST'], csrf=False)
    def myprovider_return(self, **post):
        # Extract payment info from post or get params
        reference = post.get('reference')
        status = post.get('status')  # example status param

        tx = request.env['payment.transaction'].sudo().search([('reference', '=', reference)], limit=1)
        if not tx:
            return request.render('payment.payment_error')

        if status == 'success':
            tx.sudo()._set_done()
            return request.redirect('/payment/process')
        else:
            tx.sudo()._set_canceled()
            return request.render('payment.payment_error')
