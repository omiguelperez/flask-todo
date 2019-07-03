"""Flask app."""

from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

app.config['SECRET_KEY'] = '<zlUxe@t6JO&[ngx@@}*dimYQ6&h,y'


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


@app.route('/hello')
def hello():
    """Show greeting."""
    user_ip = session.get('user_ip', None)
    todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor ']
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run()
