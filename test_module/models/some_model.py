# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SomeModel(models.Model):
    _name = 'some.model'
    _description = 'a sample model'

    name = fields.Char(
        string='Name',
        required=True
    )