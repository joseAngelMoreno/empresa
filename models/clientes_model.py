# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clientes_model(models.Model):
    _name = 'empresa.clientes_model'
    _description = 'Modelo de clientes'

    dni=fields.Char(string="Dni",required=True)
    foto=fields.Binary(string="Foto")
    nombre=fields.Char(string="Nombre",required=True)
    apellidos=fields.Char(string="Apellidos")
    telefono=fields.Char(string="Telefono")
    email=fields.Char(string="Email")