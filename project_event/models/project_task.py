# coding: utf-8 -*-
# © 2018 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class Task(models.Model):
    _name = "project.task"
    _inherit = ['project.task']

    name = fields.Char(
        string='Title',
        required=True,
    )
    code = fields.Char(
        string='Number',
    )
    activity_task_type = fields.Selection(
        [
            ('activity', 'Activity'),
            ('task', 'Task'),
        ],
        string='Type',
    )
    activity_category_id = fields.Many2one(
        'activity.category',
        string='Category',
    )
    task_category_id = fields.Many2one(
        'task.category',
        string='Category',
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Department',
    )
    employee_ids = fields.Many2many(
        'hr.employee', 'task_emp_rel',
        'task_id', 'employee_id',
        string='Employees'
    )
    responsible_id = fields.Many2one(
        'res.partner',
        related='project_id.responsible_id',
        readonly=True,
        string='Responsible',
        store=True,
    )
    partner_id = fields.Many2one(
        'res.partner',
        related='project_id.partner_id',
        string='Client',
        store=True,
        readonly=True,
    )
    task_responsible_id = fields.Many2one(
        'res.partner',
        related='parent_id.responsible_id',
        readonly=True,
        string='Responsible',
        store=True,
    )
    task_partner_id = fields.Many2one(
        'res.partner',
        related='parent_id.partner_id',
        string='Client',
        store=True,
        readonly=True,
    )
    room_id = fields.Many2one(
        string='Room',
        comodel_name='resource.calendar.room',
        ondelete='set null',
    )
    equipment_id = fields.Many2one(
        string='Equipment',
        comodel_name='resource.calendar.instrument',
        ondelete='set null',
    )
    resource_type = fields.Selection([
        ('user', 'Human'),
        ('equipment', 'Equipment'),
        ('room', 'Room')], string='Resource Type',
        default='room', required=True)

    @api.onchange('room_id')
    def _ensure_one_resource_room(self):
        if self.room_id:
            self.equipment_id = None
        elif self.equipment_id:
            self.room_id = None

    @api.onchange('equipment_id')
    def _ensure_one_resource_equipment(self):
        if self.equipment_id:
            self.room_id = None
        elif self.room_id:
            self.equipment_id = None

    @api.constrains('parent_id')
    def _check_subtask_project(self):
        for task in self:
            if task.activity_task_type is False:
                super(Task, task)._check_subtask_project()

    @api.one
    def request_resource_reservation(self):
        calendar_event = self.env['calendar.event']
        values = {
            'start': self.date_start,
            'stop': self.date_end,
            'name': self.name,
            'resource_type': self.resource_type,
            'equipment_id': self.equipment_id.id if self.equipment_id else None,
            'room_id': self.room_id.id if self.room_id else None,
             }
        calendar_event.create(values)

    @api.model
    def create(self, vals):
        if 'activity_task_type' in vals:
            if vals['activity_task_type'] == 'activity':
                vals['code'] = self.env['ir.sequence'] \
                    .next_by_code('project.task.activity')
            elif vals['activity_task_type'] == 'task':
                vals['code'] = self.env['ir.sequence'] \
                    .next_by_code('project.task.task')
        return super(Task, self).create(vals)

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name),
                      ('code', operator, name)]
        return super(Task, self).search(domain + args, limit=limit).name_get()
