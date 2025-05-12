from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_print_purchase_order(self):
        return self.env.ref('purchase_order_report.action_report_purchase_order').report_action(self)
    

    def action_print_consultation_letter(self):
        return self.env.ref('purchase_order_report.action_report_consultation_letter').report_action(self)
