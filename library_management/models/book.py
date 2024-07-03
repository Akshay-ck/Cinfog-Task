from odoo import fields, models


class Book(models.Model):
    _name = 'book'
    _description = "Book Details"

    name = fields.Char(string='Name')
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
