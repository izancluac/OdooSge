from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor'

    nombre = fields.Text()
    apellidos = fields.Text()
    numeroColegiado = fields.Integer()

    
