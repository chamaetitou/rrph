from odoo import models, fields

class SerialLabel(models.Model):
    _name = 'serial.label'
    _description = 'Serial Label'

    name = fields.Char(string='Label Name', required=True)
    status = fields.Selection([
        ('draft', 'Brouillon'),
        ('consumed', 'Consommé')
    ], default='draft')

    def action_print_label(self):
        for record in self:
            if record.status == 'draft':
                record.status = 'consumed'
            return self.env.ref('serial_label_printer.action_serial_label_report').report_action(self)
