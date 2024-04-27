from flask import Blueprint, request, send_from_directory, jsonify

from app.backend.helpers import SearchEngineHelper

main = Blueprint('main', __name__)

@main.route('/')
def serve_react_app():
    return send_from_directory('../frontend/build', 'index.html')

@main.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend/build/static', path)


@main.route('/engine_statistics')
def engine_statistics():
    counts = SearchEngineHelper.get_articles_and_dictionary_count()
    return jsonify(counts)

@main.route('/query')
def query():
    text_query = request.args.get('q')
    use_svd = request.args.get('svd') == 'true'
    max_results = int(request.args.get('max_results'))

    results_dict, times_dict = SearchEngineHelper.search_normal(text_query, use_svd, max_results)
    search_statistics = {"statistics": times_dict}
    results_dict.update(search_statistics)
    return jsonify(results_dict)