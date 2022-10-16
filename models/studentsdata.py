from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime
from datetime import date

class StudentDetails(models.Model):
    _name = "student.table"
    _description = "student details"

    dob = fields.Date(string="date of birth")

    name = fields.Char(string="NAME", help="pls enter ur name")
    reference = fields.Char(string="seqnum", required=True, readonly=True, copy=True, default=lambda self: _('New'))
    # student_age = fields.Integer(string="student_age", copy=False,compute='_get_age_from_student')
    student_age = fields.Integer(string="student_age")

    gender = fields.Selection([('male', 'MALE'), ('female', 'FEMALE')])

    image = fields.Binary(string="images")
    mark1=fields.Integer(string="mark1")
    mark2 = fields.Integer(string="mark2")
    leaving=fields.Date(string="leaving")
    # total=fields.Integer(string='total marks',compute="_calc")

    # idn_id = fields.Many2one('teacher.table',string="idn_id",ondelete="cascade")
    # idn_id = fields.Many2one('teacher.table', string="idn_id", ondelete="restrict")
    idn_id = fields.Many2one('teacher.table', string="Teacher name")

    subj_ids = fields.Many2many('subject.table', 'student_subject_rel', 'stu_id', 'teacher_id', string="subj_ids")
    # student_teacher_ids = fields.One2many('teacher.table','s_teach_id',string="manyteachers")
    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submit'),('remove','archived')], string="status")

    # @api.depends('mark1' , 'mark2')
    # def _calc(self):
    #     for rec in self:
    #         rec.total = rec.mark1 + rec.mark2

    def action_submit(self):
        for rec in self:
            # male_studentlist = self.env['student.table'].search([('gender', '=', 'male')])
            # print(male_studentlist)

            self.state = 'submit'

    def action_draft(self):
        for rec in self:

            self.state = 'draft'

    def name_get(self):
        res = []

        for rec in self:

            name = rec.name + '_' + rec.reference
            res.append((rec.id, name))


        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', ('name', operator, name),('reference', operator, name)]
        return self._search(domain + args, limit=limit)

    @api.model
    def default_get(self, fields):
        result = super(StudentDetails, self).default_get(fields)
        # print("field....",fields)
        # print("result....",result)
        # if not result.get('state'):
        result['state'] = 'draft'
        return result

    @api.constrains('student_age')
    def check_age(self):
        for rec in self:

            if rec.student_age == 0:
                raise ValidationError("age can not be zero ")

    @api.constrains('name')
    def _check_name(self):

        for rec in self:
            if rec.name.startswith("z"):
                raise ValidationError("No way!")

    @api.model
    def create(self, vals):
        print(vals)
        if not vals.get('name'):
            vals['name'] = "no name "
        # if vals.get('reference', _('New')) == _('New'):
        vals['reference'] = self.env['ir.sequence'].next_by_code('school.student')
        return super(StudentDetails, self).create(vals)

    def write(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('school.student')
        #
        # print("write is triggered", vals)

        return super(StudentDetails, self).write(vals)

    # @api.returns('self', lambda value: value.id)
    def copy(self, default=None):

        if default is None:
            default = {}
        # print(default)
        # print(default.get('name'))
        # print(self.name)

        if not default.get('name'):
            default['name'] = _("%s (copy)", self.name)
        # print(default.get('name'))

        return super(StudentDetails, self).copy(default)

    def unlink(self):
        for rec in self:
            if rec.gender == 'female':
                raise ValidationError("not way")

        return super(StudentDetails, self).unlink()

    # def unlink(self):
    #     if self.leaving != date.today():
    #         raise ValidationError("not way to delete .leaving date is today")
    #
    #
    #     return super(StudentDetails, self).unlink()

    # @api.depends('dob')
    # def _get_age_from_student(self):
    #     today_date = datetime.date.today()
    #
    #     for rec in self:
    #         if rec.dob:
    #             dob = fields.Datetime.to_datetime(rec.dob).date()
    #
    #             total_age = str(int((today_date - dob).days / 365))
    #             rec.student_age = total_age
    #         else:
    #             rec.student_age = 0

    @api.depends()
    def percent(self):
        return (self.mark1/100)*100

    # @api.model
    # def auto_remove(self):
    #
    #     data=self.env['student.table'].search([('leaving', '=', date.today())])
    #     for rec in data:
    #         if rec.leaving:
    #             rec['state'] = 'remove'
    #
    #     return True

    @api.model
    def auto_remove(self):

        data = self.env['student.table'].search([('leaving', '=', date.today())])
        for rec in data:
            if rec.leaving:
                rec['state'] = 'remove'

        return True

    @api.onchange('dob')
    def _onchange_age(self):
        for record in self:
            if record.dob:
                today = datetime.date.today()
                print(today.strftime("%m%d"))

                if today.strftime("%m%d") >= record.dob.strftime("%m%d"):
                    record['student_age'] = today.year - record.dob.year
                else:
                    record['student_age'] = today.year - record.dob.year - 1
            else:
                record['student_age'] = 0










