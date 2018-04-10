# -*- coding: utf-8 -*-

from odoo import models, fields, api


class iut_agenda(models.Model):
    _name = 'iut.agenda'
    date_start = fields.Datetime(string='debut')
    date_stop = fields.Datetime(string='fin')
    room = fields.Char(string='Salle')
    cours_id = fields.Many2one('iut.cours', string='cours')    
    classe_id = fields.Many2one('iut.classe', string='classe')    
