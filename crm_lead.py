from openerp import models, fields

class AnalyticAccount(models.Model):
    _inherit = 'crm.lead'
    other_attachments_ids = fields.Many2many('ir.attachment', string="Attached other documents")
    proposals_attachments_ids = fields.Many2many('ir.attachment', string="Attached proposal documents")

