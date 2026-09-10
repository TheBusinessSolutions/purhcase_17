# -*- coding: utf-8 -*-
from odoo import fields, models


class ServiaPurchaseRequest(models.Model):
    _name = 'servia.purchase.request'
    _description = 'Purchase Requisition'
    _order = 'needed_by desc'

    name = fields.Char('Item Requested', required=True)
    department = fields.Char('Department')
    quantity = fields.Float('Quantity')
    uom = fields.Char('Unit')
    needed_by = fields.Date('Needed By', default=fields.Date.context_today)
    est_cost = fields.Float('Estimated Cost')
    requester = fields.Char('Requested By')
    approver = fields.Char('Approved By')
    priority = fields.Selection([
        ('low', 'Low'), ('normal', 'Normal'), ('high', 'High'), ('urgent', 'Urgent'),
    ], string='Priority', default='low')
    note = fields.Text('Justification')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Approved'),
    ], default='draft')
    company_id = fields.Many2one(
        'res.company', default=lambda self: self.env.user.company_id)

    def action_confirm(self):
        for rec in self:
            rec.write({'state': 'confirmed'})

    def action_reset(self):
        for rec in self:
            rec.write({'state': 'draft'})
