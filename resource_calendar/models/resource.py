# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models

class Resource(models.Model):
    _inherit = 'resource.resource'

    resource_type = fields.Selection([
        ('user', 'Human'),
        ('material', 'Material'),
        ('room', 'Room')], string='Resource Type',
        default='user', required=True)

    room_id = fields.Many2one('resource_calendar.room', string='Room')
