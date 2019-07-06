"""Auth views."""

from flask import redirect, flash, url_for, render_template, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.firestore_service import get_user, user_put
from app.forms import LoginForm
from app.models import UserData, UserModel

from . import auth


@auth.route('/logout')
@login_required
def logout():
    """Close user session."""
    logout_user()
    flash('Come back soon!')
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['get', 'post'])
def login():
    """Return template and login."""
    login_form = LoginForm()

    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if check_password_hash(password_from_db, password):
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Welcome {}!'.format(username))

                return redirect(url_for('hello'))
            else:
                flash('Invalid credentials')
        else:
            flash('User not found')
        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Create an account."""
    signup_form = LoginForm()

    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)

            user_data = UserData(username=username, password=password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Welcome {}. Starts with your account.'.format(username))

            return redirect(url_for('hello'))
        else:
            flash('Username already exists.')

    return render_template('signup.html', **context)
