from odoo import models, fields, api

class Diagnostico(models.Model):
    _name = "hospital.diagnostico"
    _description = "El diagnostico del hospital"

    paciente_id = fields.Many2one("hospital.paciente", string = "paciente", required=True)
    doctor_id = fields.Many2one("hospital.doctor", string = "doctor", required=True)
    fecha = fields.Datetime(string = "Data", default = fields.Datetime.now)

    diagnostico = fields.Text(string = "Diagonostico")
