# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class Instrument(models.Model):
    _inherit = ['resource.resource']
    _name = 'resource_calendar.instrument'

    name = fields.Char(
        string='Name',
    )
    room_id = fields.Many2one(
        'resource_calendar.room',
        string='Room',)
    resource_id = fields.One2many(
        string='Resource Id',
        comodel_name='resource.resource',
        inverse_name='name',
    )
    sku = fields.Char(
        string='Sku',
    )
    type_id = fields.Many2one(
        string=u'type_id',
        comodel_name='model.name',
        ondelete='set null',
    )
    item_type = fields.Selection([
        ('equipment', 'Equipment'),
        ('instruments', 'Instruments'),
        ('services', 'Services'),
        ('consumables', 'Consumables'),
        ], string='Type', index=True, copy=False, default='equipment', track_visibility='onchange')
