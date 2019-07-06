"""Flask app."""

import unittest
from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.firestore_service import get_users, get_todos, put_todo
from app.forms import TodoForm

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


@app.route('/hello', methods=['get', 'post'])
@login_required
def hello():
    """Show greeting."""
    user_ip = session.get('user_ip')
    username = current_user.id

    todo_form = TodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(username),
        'username': username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        put_todo(username=username, description=todo_form.description.data)
        flash('Task created!')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run()
