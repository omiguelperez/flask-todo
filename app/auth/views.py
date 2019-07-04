"""Auth views."""

from flask import redirect, flash, url_for, render_template, session

from app.forms import LoginForm

from . import auth


@auth.route('/login', methods=['get', 'post'])
def login():
    """Return template and login."""
    login_form = LoginForm()

    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('User registered successfully!')

        return redirect(url_for('index'))

    return render_template('login.html', **context)
