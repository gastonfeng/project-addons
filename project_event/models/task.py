# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Task(models.Model):
    _name = 'project.task'
    _inherit = ['project.task']

    task_date_start = fields.Datetime(
        string='Starting Date',
        default=fields.Datetime.now,
        index=True,
        copy=False,
    )
