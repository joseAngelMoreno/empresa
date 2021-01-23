# -*- coding: utf-8 -*-

from odoo import models, fields, api

class productos_model(models.Model):
    _name = 'empresa.productos_model'
    _description = 'Modelo de productos'

    nombre=fields.Char(string="Nombre del producto")
    descripcion=fields.Char(string="Descripcion")
    pvp=fields.Float(string="Precio")