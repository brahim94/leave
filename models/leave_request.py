# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class Leave_request(models.Model):
    _inherit = 'hr.leave'
    _description = 'Demande de congé'

    
    phone_number = fields.Char(string='N° Téléphone')
    #phone_number_work = fields.Char(string='N° Téléphone')
    ville = fields.Char(string='Ville')
    matricule_employee = fields.Many2one('hr.job', string="Matricule")
    interim_employee = fields.Many2one('hr.employee', string="Employé en intérim")

    @api.onchange('employee_id')
    def onchange_employee_id(self):
        self.phone_number = self.employee_id.mobile_phone
        #self.phone_number_work = self.employee_id.work_phone
        self.ville = self.employee_id.work_location
        self.matricule_employee = self.employee_id.job_id
        



    def print_leave_request(self):
            return self.env.ref('tech_leave.action_report_leave').report_action(self)

    