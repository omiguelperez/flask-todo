"""Flask app."""

import unittest
from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import get_users, get_todos

app = create_app()


@app.cli.command()
def test():
    """Run todo app tests."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


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


@app.route('/hello', methods=['get'])
@login_required
def hello():
    """Show greeting."""
    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'todos': get_todos(username),
        'username': username
    }

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run()
