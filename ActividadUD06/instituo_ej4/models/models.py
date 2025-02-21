# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CicleFormatiu(models.Model):
    _name = 'instituto.cicle'
    _description = 'Cicle Formatiu'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Descripció')
    modul_ids = fields.One2many('instituto.modul', 'cicle_id', string='Mòduls')

class Modul(models.Model):
    _name = 'instituto.modul'
    _description = 'Mòdul'

    name = fields.Char(string='Nom', required=True)
    cicle_id = fields.Many2one('instituto.cicle', string='Cicle Formatiu', required=True)
    professor_id = fields.Many2one('instituto.professor', string='Professor')
    alumne_ids = fields.Many2many('instituto.alumne', string='Alumnes Matriculats')

class Alumne(models.Model):
    _name = 'instituto.alumne'
    _description = 'Alumne'

    name = fields.Char(string='Nom', required=True)
    age = fields.Integer(string='Edat')
    modul_ids = fields.Many2many('instituto.modul', string='Mòduls Matriculats')

class Professor(models.Model):
    _name = 'instituto.professor'
    _description = 'Professor'

    name = fields.Char(string='Nom', required=True)
    modul_ids = fields.One2many('instituto.modul', 'professor_id', string='Mòduls Impartits')
