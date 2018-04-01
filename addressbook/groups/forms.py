from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import Required, Optional

__all__ = ['NewGroupForm', 'UpdateGroupForm']


class NewGroupForm(FlaskForm):
    name = TextField('Name', validators=[Required()])


class UpdateGroupForm(FlaskForm):
    name = TextField('Name', validators=[Optional()])
