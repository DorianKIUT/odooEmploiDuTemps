# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class iut_eleve(models.Model):
    _name = 'iut.eleve'

    name = fields.Char(string='nom')
    surname = fields.Char(string='prénom')
    birthdate = fields.Date(string='date de naissance')
    age = fields.Integer(compute='_compute_age_eleve', string='age')
    classe_id = fields.Many2one('iut.classe', string='classe')

    @api.depends('birthdate')
    def _compute_age_eleve(self):
        for record in self:
            if record.birthdate:
                year_student = record.birthdate.split('-')[0]
                month_student = record.birthdate.split('-')[1]
                day_student = record.birthdate.split('-')[2]
                age_student = self.calculate_age_student(year_student, month_student, day_student)
                record.age = age_student

    def calculate_age_student(self, year_student, month_student, day_student):
        date_now = datetime.now()
        year_now = date_now.year
        month_now = date_now.month
        day_now = date_now.day
        age_year = int(year_now) - int(year_student)
        if month_now > int(month_student):
            pass
        elif month_now <= int(month_student):
            if day_now > int(day_student):
                pass
            else:
                age_year = age_year - 1
        else:
            age_year = age_year - 1
        return age_year
