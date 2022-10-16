from odoo import api, fields, models


class CreatethestudentWiz(models.TransientModel):
    _name = "createthe.student.wizard"
    _description = "create student wizard"



    text = fields.Char(string="your suggesions")


    def action_createthe(self):
        print("clicked")

