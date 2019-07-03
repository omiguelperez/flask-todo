"""Flask app."""

from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
boostrap = Bootstrap(app)

app.config['SECRET_KEY'] = '<zlUxe@t6JO&[ngx@@}*dimYQ6&h,y'


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


@app.errorhandler(404)
def not_found(error):
    """Handle 404 error."""
    return render_template('404.html', error=error)


@app.route('/')
def index():
    """Set user ip in browser cookie and redirect hello view."""
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['get', 'post'])
def hello():
    """Show greeting."""
    user_ip = session.get('user_ip')
    username = session.get('username')
    todos = [
        'Comprar cafe', 
        'Enviar solicitud de compra', 
        'Entregar video a productor '
    ]
    login_form = LoginForm()

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('User registered successfully!')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run()
