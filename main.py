"""Flask app."""

from flask import Flask, request, redirect, make_response, render_template

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Handle 404 error."""
    return render_template('404.html', error=error)


@app.route('/')
def index():
    """Set user ip in browser cookie and redirect hello view."""
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    """Show greeting."""
    user_ip = request.cookies.get('user_ip', None)
    todos = ['Todo #1', 'Todo #2', 'Todo #3']
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)


if __name__ == "__main__":
    app.run()
