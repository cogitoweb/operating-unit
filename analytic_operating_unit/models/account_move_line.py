# -*- coding: utf-8 -*-
# © 2016-17 Eficent Business and IT Consulting Services S.L.
# © 2016-17 Serpent Consulting Services Pvt. Ltd.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import fields, models


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    operating_unit_id = fields.Many2one(
        related="analytic_account_id.operating_unit_id",
        store=True
    )
