from openerp import models, fields, api

class Lead(models.Model):
    _inherit = 'crm.lead'

    other_attachments_ids = fields.Many2many('ir.attachment', string="Attached other documents")
    proposals_attachments_ids = fields.Many2many('ir.attachment', string="Attached proposal documents")

    planned_revenue_periodically = fields.Float(string="Expected periodical revenue")
    planned_revenue_period = fields.Selection([('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly')
    planned_revenue_yearly = fields.Float(string="Yearly periodical revenue", compute='_compute_revenue_yearly')

    @api.depends('planned_revenue_periodically', 'planned_revenue_period')
    def _compute_revenue_yearly(self):
        for record in self:
            if (record.planned_revenue_period == 'daily'):
                record.planned_revenue_yearly = 20 * 12 * record.planned_revenue_periodically
            if (record.planned_revenue_period == 'monthly'):
                record.planned_revenue_yearly = 12 * record.planned_revenue_periodically
            if (record.planned_revenue_period == 'yearly'):
                record.planned_revenue_yearly = record.planned_revenue_periodically

    planned_revenue_total_first_year = fields.Float(compute='_compute_revenue_total_first_year')
    @api.depends('planned_revenue_yearly', 'planned_revenue')
    def _compute_revenue_total_first_year(self):
        for record in self:
            record.planned_revenue_total_first_year = record.planned_revenue_yearly + record.planned_revenue
