from flask import Blueprint, request, send_from_directory

from app.backend.helpers import SearchEngineHelper

main = Blueprint('main', __name__)

@main.route('/')
def serve_react_app():
    return send_from_directory('../frontend/build', 'index.html')

@main.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend/build/static', path)

@main.route('/query')
def query():
    text_query = request.args.get('q')
    use_svd = request.args.get('svd') == 'true'
    max_results = int(request.args.get('max_results'))

    json_result = SearchEngineHelper.search_normal(text_query, use_svd, max_results)
    return json_result