# -*- coding: utf-8 -*-

from odoo import models, fields, api


class empresa(models.Model):
    _name = 'empresa.facturas_model'
    _description = 'Modelo de facturas'

    ref=fields.Char(string="Referencia" ,required=True)
    fecha=fields.Char(string="Fecha" )
    iva=fields.Float(string="IVA")
    base=fields.Float(string="Base")
    total=fields.Float(string="Total")