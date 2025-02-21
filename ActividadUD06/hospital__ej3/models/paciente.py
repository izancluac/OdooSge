# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'

    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string = "Apellidos", required=True)
    sintoma = fields.Text(string = "Sintomas")

   



