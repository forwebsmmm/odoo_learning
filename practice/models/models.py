# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class practice(models.Model):
    _name = 'practice.practice'
    _description = 'practice.practice'
    _rec_name = 'description'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.constrains('value')
    def _check_value(self):
        for r in self:
            if r.value > 20:
                raise exceptions.ValidationError(
                    "value more than 20")
