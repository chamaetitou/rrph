from odoo import models, fields, api

class SerialLabelWizard(models.Model):
    _inherit = 'ir.sequence'


    is_label_code = fields.Boolean("Serial Number Sequence")
