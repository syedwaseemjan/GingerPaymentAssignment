from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required, Optional

__all__ = ['NewGroupForm', 'UpdateGroupForm']


class NewGroupForm(Form):
    name = TextField('Name', validators=[Required()])


class UpdateGroupForm(Form):
    name = TextField('Name', validators=[Optional()])
