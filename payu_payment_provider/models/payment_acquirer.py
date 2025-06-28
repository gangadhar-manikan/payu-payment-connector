from odoo import models, fields, api, _

class PaymentAcquirerMyProvider(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('myprovider', 'MyProvider')], ondelete={'myprovider': 'set default'})
    myprovider_merchant_id = fields.Char(string='Merchant ID', required_if_provider='myprovider')
    myprovider_merchant_key = fields.Char(string='Merchant Key', required_if_provider='myprovider')

    def _get_myprovider_urls(self):
        """ Return URLs for MyProvider endpoints """
        if self.environment == 'prod':
            return {
                'payment_url': 'https://pay.myprovider.com/checkout',
                'validate_url': 'https://pay.myprovider.com/api/validate',
            }
        else:
            return {
                'payment_url': 'https://sandbox.pay.myprovider.com/checkout',
                'validate_url': 'https://sandbox.pay.myprovider.com/api/validate',
            }

    def _myprovider_form_generate_values(self, values):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        myprovider_tx_values = dict(values)
        myprovider_tx_values.update({
            'merchant_id': self.myprovider_merchant_id,
            'amount': values['amount'],
            'currency': values['currency'].name,
            'reference': values['reference'],
            'partner_email': values.get('partner_email'),
            'return_url': '%s/payment/myprovider/return' % base_url,
        })
        return myprovider_tx_values

    def _myprovider_get_form_action_url(self):
        return self._get_myprovider_urls()['payment_url']

    def myprovider_form_generate_values(self, values):
        return self._myprovider_form_generate_values(values)
