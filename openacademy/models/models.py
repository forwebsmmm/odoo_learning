# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class AcademyClass(models.Model):
    _name = 'academy.class'

    name = fields.Char('Name')
    level = fields.Selection([
        ('1', 'Newbie'),
        ('2', 'Middle'),
        ('3', 'Pro')
    ], string='Level')
    session_ids = fields.One2many('academy.session',
                                  'class_id',
                                  string='Sessions',
                                  ondelete='cascade')


class AcademySession(models.Model):
    _name = 'academy.session'

    name = fields.Char('Name')
    subject = fields.Char('Subject')
    # instructor_id = fields.Many2one('res.partner', string='Maesters')
    start_date = fields.Datetime(string='Start date')
    room_size = fields.Integer(string='Room size')
    # student_ids = fields.Many2many('res.partner', string='Attendees')
    class_id = fields.Many2one('academy.class', string='Class')
    # active = fields.Boolean(string='Active?', default=True)
