import json
import time

from app.engine.description_extractor import DescriptionExtractor
from app.engine.search_engine import SearchEngine


class SearchEngineHelper:
    engine = SearchEngine()
    url_format = 'https://simple.wikipedia.org/wiki/{article}'


    @staticmethod
    def get_articles_and_dictionary_count():
        out = {
            'article_count': SearchEngineHelper.engine.get_article_count(),
            'dictionary_count': SearchEngineHelper.engine.get_dictionary_count()
        }
        return out

    @staticmethod
    def search_normal(text_query, use_svd=False, max_results=10):
        start_time = time.time()
        results = SearchEngineHelper.engine.search(text_query, method='SVD' if use_svd else 'NORMAL', max_results=max_results)
        search_time = time.time() - start_time

        results_array = []
        start_creation = time.time()
        for article_name, similarity in results:
            results_array.append({
                "name": article_name,
                "similarity": similarity,
                "url": SearchEngineHelper.url_format.format(article=article_name.replace(' ', '_')),
                "description": DescriptionExtractorHelper.extract(article_name)
            })
        creation_time = time.time() - start_creation

        times_dict = {"search_time": search_time, "creation_time": creation_time}
        results_dict = {"results": results_array}

        return results_dict, times_dict

class DescriptionExtractorHelper:
    extractor = DescriptionExtractor()
    @staticmethod
    def extract(article_name):
        return DescriptionExtractorHelper.extractor.get_description(article_name)
