from odoo import api, fields, models


class Session(models.Model):
    _name = 'arisnew.session'
    _description = 'Data Course Session..'

    name = fields.Char(string='Name')
    course_id = fields.Many2one(
        comodel_name='arisnew.course', 
        string='Course'
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Instructor',
        domain="[('is_instructor', '=', True)]",
    )

    session_date = fields.Datetime(
        string='Session Date', 
        default=fields.Datetime.now()
    )
    
    min_attendee = fields.Integer(
        string='Minimum Attendee'
    )

    attendee_ids = fields.One2many(
        comodel_name='arisnew.attendee',
        inverse_name='session_id',
        string='Attendee'
    )
    
    
class Attendee(models.Model):
    _name = 'arisnew.attendee'
    _description = 'Attendee of course session....'

    name = fields.Char(string='No Reg')
    student_id = fields.Many2one(
        comodel_name='res.partner', 
        domain="[('is_student', '=', True)]",
        string='Student'
    )
    reg_date = fields.Datetime(
        string='Reg Date',
        default=fields.Datetime.now(),
    )
    session_id = fields.Many2one(
        comodel_name='arisnew.session',
        string='Session'
    )
    remark = fields.Char(string='Remarks')