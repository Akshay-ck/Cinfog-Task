from odoo import models, fields


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    customer_reference = fields.Char(string='Customer Reference')

    def automated_action_send_mail(self):
        action = self.env.ref('library_management.action_auto_mail_sale_confirm')
        action.with_context(active_model='sale.order',
                                   active_ids=[self.id]).run()
