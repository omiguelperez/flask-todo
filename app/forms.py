"""Forms."""

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


class TodoForm(FlaskForm):
    """Todo form."""

    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Send')


class DeleteTodoForm(FlaskForm):
    """Delete todo form."""

    submit = SubmitField('Remove')
