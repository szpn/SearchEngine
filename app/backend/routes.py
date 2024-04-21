from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, World!'

@main.route('/about')
def about():
    return 'About Page'
