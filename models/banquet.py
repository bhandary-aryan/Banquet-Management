from odoo import models, fields


class Banquet(models.Model):
    _name = 'banquet.management'
    _description = 'Banquet Management'

    name = fields.Char(string='Banquet Name', required=True)
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    location = fields.Char(string='Location', required=True)
    attendees = fields.Integer(string='Number of Attendees', required=True)
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)
