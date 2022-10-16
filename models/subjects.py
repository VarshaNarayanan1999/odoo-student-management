from odoo import api, fields, models, _
from datetime import date,datetime
from dateutil.relativedelta import relativedelta


class SubjectDetails(models.Model):
    _name = 'subject.table'
    _description = "subject details"

    _rec_name = 'subject_name'
    subject_name = fields.Char(string="subject_name")
    # dob = fields.Date('DOB')
    # age = fields.Char('Age')

    # @api.onchange('dob')
    # def set_age(self):
    #     for rec in self:
    #         if rec.dob:
    #             dt = rec.dob
    #             d1 = datetime.strptime(dt,"%Y-%m-%d").date()
    #
    #
    #             d2 = date.today()
    #
    #             rd = relativedelta(d2, d1)
    #             rec.age = str(rd.years) + ' years'
