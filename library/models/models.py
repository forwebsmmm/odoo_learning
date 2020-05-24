# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class LibBook(models.Model):
    _name = 'lib.book'

    name = fields.Char('Name')
    year = fields.Selection(
        [(str(num), str(num)) for num in
         range(1900, (datetime.now().year) + 1)],
        'Year')
    author_ids = fields.Many2many('lib.author', string='Authors')
    editor_ids = fields.Many2many('lib.editor', string='Editors')
    isbn = fields.Char('ISBN')
    history = fields.One2many('lib.history', 'book_id', string='Book history')
    customer_id = fields.Many2one('lib.customer', string='Customer')


class LibAuthor(models.Model):
    _name = 'lib.author'

    name = fields.Char('First name')
    surname = fields.Char('Surname')


class LibEditor(models.Model):
    _name = 'lib.editor'

    name = fields.Char('First name')
    surname = fields.Char('Surname')

class LibCustomer(models.Model):
    _name = 'lib.customer'

    name = fields.Char('First name')
    surname = fields.Char('Surname')
    address = fields.Char('Address')
    email = fields.Char('Email')
    book_ids = fields.One2many('lib.book', 'customer_id', string='Books')

class LibHistory(models.Model):
    _name = 'lib.history'

    book_id = fields.Many2one('lib.book', string='Book')
    date_out = fields.Datetime(string='Date out', default=fields.Datetime.now)
    date_in = fields.Datetime(string='Date in')
    # inlib = fields.Boolean(string='Book in Library?', default=True)
    customer_id = fields.Many2one('lib.customer', string='Customer')