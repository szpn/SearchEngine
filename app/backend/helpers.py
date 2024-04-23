import json

from app.engine.search_engine import SearchEngine

class SearchEngineHelper:
    engine = SearchEngine()
    url_format = 'https://simple.wikipedia.org/wiki/{article}'

    @staticmethod
    def search_normal(text_query):
        results = SearchEngineHelper.engine.search(text_query, method='NORMAL')
        out = []
        for article_name, similarity in results:
            out.append({
                "name": article_name,
                "similarity": similarity,
                "url": SearchEngineHelper.url_format.format(article=article_name.replace(' ', '_')),
                "description": "none"
            })

        json_data = json.dumps(out)
        return json_data
