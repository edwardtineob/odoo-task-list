# -*- coding: utf-8 -*-

from odoo import models, fields

class Item(models.Model):
    _name = 'todo.item'
    _description = 'To-do Item'
    name = fields.Char('Description', required=True)
    active = fields.Boolean('Active?', default=True)