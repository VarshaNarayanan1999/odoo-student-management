from odoo import api, fields, models


class CreatestudentWiz(models.TransientModel):
    _name = "create.student.wizard"
    _description = "create student wizard"



    name = fields.Char(string="NAME", help="pls enter ur name")

    def action_create(self):
        print("clicked")



