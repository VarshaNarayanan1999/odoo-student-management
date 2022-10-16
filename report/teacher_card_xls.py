from odoo import models, fields, _
class teacherReportXlsx(models.AbstractModel):
    _name = 'report.teacher_id_card'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, teachers):
        sheet = workbook.add_worksheet('teacher card')
        bold = workbook.add_format(
            {'bold': True, 'font_color': 'blue', 'align': 'left', 'border': 7, 'border_color': 'red'})
        date_style = workbook.add_format(
            {'text_wrap': True, 'font_color': 'black', 'num_format': 'dd-mm-yyyy', 'align': 'right', 'border': 7,
             'border_color': 'red'})
        bold2 = workbook.add_format(
            {'bold': True, 'font_color': 'black', 'align': 'left', 'border': 7, 'border_color': 'red'})
        bold3 = workbook.add_format({'bold': True, 'font_color': 'red', 'align': 'center', 'bg_color': 'yellow'})
        # format1 = workbook.add_format({'italic': True, 'underline': True})
        bold5 = workbook.add_format(
            {'bold': True, 'font_color': 'black', 'align': 'right', 'border': 7, 'border_color': 'red'})
        sheet.set_column('A:B', 15)
        sheet.set_column('C:D', 8)
        sheet.set_column('E:F', 8)
        sheet.set_column('G:H', 8)
        sheet.set_column('I:J', 8)
        sheet.set_column('I:J', 8)




        sheet.merge_range('A1:N1', 'TEACHER DETAILS', bold3)
        row = 1
        col = 0

        sheet.merge_range(row, col, row, col + 1, 'STUDENTS', bold)
        col = col + 2

        for object in teachers:
            row = row + 1
            col = 0
            li = []
            for rec in object.stu_teacher_ids:
                li.append(rec.name)
                sheet.merge_range(row, col, row, col + 1, ','.join(li), bold2)
