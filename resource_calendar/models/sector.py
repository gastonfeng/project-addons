# -*- coding: utf-8 -*-
# Copyright 2018 Savoir-faire Linux
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models

class Sector(models.Model):
    _name = 'resource_calendar.sector'

    name = fields.Char(
        string='Name',
    )
