from odoo import models, fields, _


class StudentReportXlsx(models.AbstractModel):
    _name = 'report.student_id_card'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, students):
        sheet = workbook.add_worksheet('students card')
        bold = workbook.add_format({'bold': True, 'font_color': 'blue', 'align': 'left','border':7,'border_color':'red'})
        date_style = workbook.add_format({'text_wrap': True,'font_color': 'black','num_format': 'dd-mm-yyyy', 'align': 'right','border':7,'border_color':'red' })
        bold2 = workbook.add_format({'bold': True, 'font_color': 'black', 'align': 'left','border':7,'border_color':'red'})
        bold3 = workbook.add_format({'bold': True, 'font_color': 'red', 'align': 'center', 'bg_color': 'yellow'})
        # format1 = workbook.add_format({'italic': True, 'underline': True})
        bold5 = workbook.add_format({'bold': True, 'font_color': 'black', 'align': 'right', 'border': 7, 'border_color': 'red'})
        sheet.set_column('A:B', 8)
        sheet.set_column('C:D', 8)
        sheet.set_column('E:F', 8)
        sheet.set_column('G:H', 8)
        sheet.set_column('I:J',8)
        sheet.set_column('Q:R', 15)

        sheet.merge_range('A1:N1','STUDENT DETAILS', bold3)
        row = 1
        col = 0


        sheet.merge_range(row, col, row, col + 1, 'NAME',bold)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'AGE', bold)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'Dob', bold)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'Gender', bold)
        col = col + 2

        sheet.merge_range(row, col, row, col + 1, 'Mark1', bold)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'Mark2', bold)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'Total', bold)
        col=col+2
        sheet.merge_range(row, col, row, col + 1, 'Teacher name', bold)
        col=col+2
        sheet.merge_range(row, col, row, col + 1, 'Subjectname', bold)

        for object in students:
            row=row+1
            col=0
            print(object)
            sheet.merge_range(row, col, row, col + 1, object.name,bold2)
            col += 2
            sheet.merge_range(row, col, row, col + 1, object.student_age,bold5)
            col += 2
            sheet.merge_range(row, col, row, col + 1, object.dob, date_style)
            col += 2


            # gndr = dict([('male', 'MALE'), ('female', 'FEMALE')])
            # gndrout = str(gndr[object.gender])
            # sheet.merge_range(row, col, row, col + 1, gndrout,bold2)

            gen=dict(object._fields['gender'].selection).get(object.gender) or False
            sheet.merge_range(row, col, row, col + 1, gen, bold2)


            col=col+2

            sheet.merge_range(row, col,row, col + 1, object.mark1,bold5)
            col += 2
            sheet.merge_range(row, col, row, col + 1,object.mark2,bold5)
            col += 2
            total=object.mark1 + object.mark2

            sheet.merge_range(row, col,row,col+1, total,bold5)

            col=col+2
            sheet.merge_range(row, col, row, col + 1,object.idn_id.teacher_name,bold2)

            col=col+2
            # for rec in object.subj_ids:
            #     sheet.merge_range(row, col, row, col + 1, ','.join(rec.subject_name), bold2)
            #     col=col+1
            l=[]

            for rec in object.subj_ids:
                l.append(rec.subject_name)
                sheet.merge_range(row, col, row, col + 1, ','.join(l),bold2)



            # sheet.merge_range(row, col, row, col + 1,object.subj_ids.subject_name,bold2)


            # for val in object.subj_ids.subject_name:
            #     sheet.merge_range(row, col, row, col + 1,val,bold2)

            # sheet.merge_range(row, col, row, col + 1, ', '.join(object.idn_id.mapped('idn_id.name')))

            # for object in students:
            #
            #     row=row+1
            #
            #     sheet.merge_range(row,col,row,col+1,object.reference,bold3)
            #     row = row+1
            #     sheet.write(row,col,'Name',bold)
            #     sheet.write(row,col+1,object.name)
            #     row +=1
            #     sheet.write(row, col, 'Age', bold)
            #     sheet.write(row, col + 1, object.student_age,bold2)
            #     row += 1
            #     sheet.write(row, col, 'Gender', bold)
            #     sheet.write(row, col + 1, object.gender)
            #
            #     row +=1
            #
            #     sheet.write(row, col, 'Dob',bold)
            #     sheet.write(row, col + 1, object.dob,date_style)
            #
            #     row += 2

            # sheet.write(row, col, object.name)
            # sheet.write(row, col, object.dob,date_style)
            # sheet.write(row, col, object.mark1)
            # sheet.write(row, col, object.mark2)
            # sheet.write(row, col, object.total)

    #
    # sheet.write(row, col, 'Name', bold)
    # # sheet.write(row,col+1,object.name)
    # row += 1
    # sheet.write(row, col, 'Age', bold)
    # sheet.write(row, col + 1, object.student_age, bold2)
    # row += 1
    # sheet.write(row, col, 'Gender', bold)
    # sheet.write(row, col + 1, object.gender)
    #
    # row += 1
    #
    # sheet.write(row, col, 'Dob', bold)
    # sheet.write(row, col + 1, object.dob, date_style)
    #
    # row += 2


