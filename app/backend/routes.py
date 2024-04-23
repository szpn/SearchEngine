from flask import Blueprint, request, jsonify

from app.backend.helpers import SearchEngineHelper

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Hello, World!'

@main.route('/query')
def query():
    text_query = request.args.get('q')
    use_svd = request.args.get('svd') == 'true'
    print(use_svd)
    max_results = int(request.args.get('max_results'))

    json_result = SearchEngineHelper.search_normal(text_query, use_svd, max_results)
    return json_result