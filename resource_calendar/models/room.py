# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class Room(models.Model):
    _inherit = ['resource.resource']
    _name = 'resource_calendar.room'

    id_room = fields.Char(
        string='Room ID',
    )
    name = fields.Char(
        string='Name'
    )
    capacity = fields.Integer(
        string='Capacity',
    )
    description = fields.Text(
        string='Dsescription',
    )
    room_type = fields.Many2one(
        string='Room Type',
        comodel_name='resource_calendar.room_type',
        ondelete='set null',
    )
    is_bookable = fields.Boolean(
        string='Is Bookable',
    )
    sector = fields.Many2one(
        string='Sector',
        comodel_name='resource_calendar.sector',
        ondelete='set null',
    )
    instruments_ids = fields.One2many(
        'resource_calendar.instrument',
        'room_id',
        string='Instruments',
    )
    resource_id = fields.One2many(
        string='Resource Id',
        comodel_name='resource.resource',
        inverse_name='name',
    )
    # TODO: Pricind field model ? field

    @api.model
    def create(self, values):
        """
            Create a new record for a model Room
            @param values: provides a data for new record
            @return: returns a id of new record
        """
        values['resource_type'] = 'room'
        result = super().create(values)
        return result
