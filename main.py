"""Flask app."""

from flask import Flask, request, redirect, make_response

app = Flask(__name__)


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
    user_ip  = request.cookies['user_ip']
    return 'Hello! Your ip is {}'.format(user_ip)


if __name__ == "__main__":
    app.run()
