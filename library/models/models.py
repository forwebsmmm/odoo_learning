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

class LibHistory(models.Model):
    _name = 'lib.history'

    book_id = fields.Many2one('lib.book', string='Book')
    date = fields.Datetime(string='Date')
    inlib = fields.Boolean(string='Book in Library?', default=True)
    customer_id = fields.Many2one('lib.customer', string='Customer')