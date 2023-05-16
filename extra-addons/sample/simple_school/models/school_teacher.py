from odoo import fields, models, api, _


class SchoolTeacher(models.Model):
    _name = 'school.teacher'

    name = fields.Char()
    birthday = fields.Date()

