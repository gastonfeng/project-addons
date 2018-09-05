# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models

class Instrument(models.Model):
    _inherit = ['resource.resource']
    _name = 'resource_calendar.instrument'

    name = fields.Char(
        string='Name',
    )
    room_id = fields.Many2one(
        string='Room',
        comodel_name='resource_calendar.room',
        inverse_name='name'
    )
    resource_id = fields.One2many(
        string='Resource Id',
        comodel_name='resource.resource',
        inverse_name='name',
    )
