# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Leave_request(models.Model):
    _inherit = 'hr.leave'
    _description = 'Demande de congé'

def print_leave_request(self):
        return self.env.ref('tech_leave.action_report_leave').report_action(self)