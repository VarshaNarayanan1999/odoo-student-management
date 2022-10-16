from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
from datetime import date


class TeacherDetails(models.Model):
    # _inherit = "student.table"
    _name = "teacher.table"
    _description = "Teacher details"

    # _rec_name = 'teacher_name'
    student_age = fields.Integer(string="student_age")

    teacher_name = fields.Char(string="TEACHER NAME")
    teacher_middle_name = fields.Char(string="teacher middle name")

    gender = fields.Selection([('male', 'MALE'), ('female', 'FEMALE')])
    # st_age = fields.Integer(string="AGE")

    image = fields.Binary(string="images")

    # gender = fields.Selection(selection_add=[('other', 'OTHER')],)

    s_teach_id = fields.Many2one("student.table")
    stu_teacher_ids = fields.One2many('student.table', 'idn_id', string="stu_teacher_ids")
    # teach_sub_id = fields.Many2one('subject.table',ondelete="set default")
    teach_sub_id = fields.Many2one('subject.table')

    student_count = fields.Integer(string="student_count", compute="_compute_student_count")
    student_c = fields.Integer(string="student_c", compute="_compute_student")

    def name_get(self):
        res = []

        for rec in self:

            name = rec.teacher_name + rec.teacher_middle_name
            res.append((rec.id, name))


        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', ('teacher_name', operator, name), ('teacher_middle_name', operator, name)]
        return self._search(domain + args, limit=limit)


    def _compute_student_count(self):
        for rec in self:
            print(rec)
            student_count = self.env['student.table'].search_count([('idn_id', '=', rec.id)])
            rec.student_count = student_count

    @api.depends()
    def _compute_student(self):
        for rec in self:
            print(rec)
            student_c = self.env['student.table'].search_count([('name', '=', 'DEEPU')])
            rec.student_c = student_c
            print("the number of students with the name","deepu",rec.student_c)

    @api.onchange('s_teach_id')
    def onchange_s_teach_id(self):
        if self.s_teach_id and self.s_teach_id.gender and self.s_teach_id.student_age:
            self.gender = self.s_teach_id and self.s_teach_id.gender or ''
            self.student_age = self.s_teach_id and self.s_teach_id.student_age or ''

    # @api.constrains('teacher_name')
    # def check_name(self):
    #     for rec in self:
    #         condition = self.env['teacher.table'].search([('teacher_name', '=', rec.teacher_name)])
    #         if condition:
    #             raise ValidationError("Name %s already exist" % rec.teacher_name)
    #
    #
    # @api.depends()
    def get_per(self):
        max_count=10

        valu=self.student_count/max_count*100

        return valu










