from odoo import models, fields, api

class SerialLabelWizard(models.TransientModel):
    _name = 'serial.label.wizard'
    _description = 'Serial Label Wizard'

    label_type = fields.Many2one('ir.sequence', string='Label type', required=True)
    number_of_labels = fields.Integer(string='Number of Labels', required=True)

    def generate_labels(self):
        self.ensure_one()
        labels = []
        sequence_code = self.label_type.code
        for i in range(self.number_of_labels):
            sequence = self.env['ir.sequence'].next_by_code(sequence_code)
            label = self.env['serial.label'].create({
                'name': sequence,
                'status': 'consumed'
            })
            labels.append(label.id)
        return self.env.ref('serial_label_printer.action_serial_label_report').report_action(labels)
