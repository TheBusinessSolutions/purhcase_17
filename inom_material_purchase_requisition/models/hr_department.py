# -*- coding: utf-8 -*-
from odoo import models, fields

class HrDepartment(models.Model):
    _inherit = 'hr.department'

    requisition_stock_location_id = fields.Many2one(
        'stock.location',
        string='Destination Location',
        domain="[('usage', 'in', ('internal', 'customer'))]",
        help='Default destination location for material requisitions of this department.',
    )