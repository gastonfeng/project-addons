# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']

    client_type = fields.Many2one(
        'res.partner.category',
        string='Client Type',
        related='category_id.client_type',
        track_visibility='onchange',
    )
    sector_id = fields.Many2one(
        'res.partner.sector',
        string='Faculty Sectors',
        track_visibility='onchange',
    )
