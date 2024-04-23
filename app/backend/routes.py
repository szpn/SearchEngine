from flask import Blueprint, request, jsonify

from app.backend.helpers import SearchEngineHelper

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, World!'

@main.route('/query')
def query():
    text_query = request.args.get('q')

    json_result = SearchEngineHelper.search_normal(text_query)
    return json_result