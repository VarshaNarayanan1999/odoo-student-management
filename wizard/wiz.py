from odoo import api, fields, models


class WizCreate(models.TransientModel):
    _name = "the.wizard"
    _description = "the wizard"

    text = fields.Char(string="your email .....")

