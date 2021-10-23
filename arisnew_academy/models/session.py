from odoo import api, fields, models, exceptions


class Session(models.Model):
    _name = 'arisnew.session'
    _inherit = 'mail.thread'
    _description = 'Data Course Session..'

    name = fields.Char(string='Name', track_visibility='onchange')
    course_id = fields.Many2one(
        comodel_name='arisnew.course', 
        string='Course',
        track_visibility='onchange'
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Instructor',
        domain="[('is_instructor', '=', True)]",
        track_visibility='onchange'
    )

    session_date = fields.Datetime(
        string='Session Date', 
        default=fields.Datetime.now(),
        track_visibility='onchange'
    )
    
    min_attendee = fields.Integer(
        string='Minimum Attendee',
        track_visibility='onchange'
    )

    attendee_ids = fields.One2many(
        comodel_name='arisnew.attendee',
        inverse_name='session_id',
        string='Attendee'
    )

    taken_seats = fields.Float(
        compute='_compute_taken_seats', 
        string='Taken Seats',
        store=True,
    )

    state = fields.Selection(string='State', selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], readonly=True, default='draft', required=True, track_visibility='onchange')

    def action_confirm(self):
        # validasi
        # manipulasi
        self.write({'state': 'confirm'})

    def action_done(self):
        # validasi
        # manipulasi
        self.write({'state': 'done'})

    def action_cancel(self):
        # validasi
        # manipulasi
        self.write({'state': 'cancel'})

    def action_reset(self):
        # validasi
        # manipulasi
        self.write({'state': 'draft'})

    @api.multi
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise exceptions.UserError('Tidak bisa hapus data selain Draft')
        return super(Session, self).unlink()
    
    
    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.min_attendee
    
    @api.onchange('min_attendee', 'attendee_ids')
    def _onchange_attendee(self):
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Salah Data!",
                    'message': "Min Attendee tidak boleh kurang dari 0",
                },
            }
        if self.min_attendee < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase min attendee or remove excess attendees",
                },
            }

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Nama Session harus unik, tidak boleh sama!!!!"),
    ]

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            students = [record.student_id.id for record in r.attendee_ids]
            if r.instructor_id and r.instructor_id.id in students:
                raise exceptions.ValidationError("Instructor tidak boleh menjadi Attendee...!!!")
    


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