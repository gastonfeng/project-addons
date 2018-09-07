# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class RoomType(models.Model):
    _name = 'resource_calendar.room_type'

    name = fields.Char(
        string='Room Type'
    )
