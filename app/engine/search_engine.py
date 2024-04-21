import numpy as np
import scipy as sp

from data_processing.TextSanitizer import TextSanitizer


class SearchEngine:
    def __init__(self):
        self.dictionary_path = "data/dictionary.txt"
        self.search_matrix_path = "data/term_by_document.npz"
        self.search_matrix_SVD_pah = "data/US_vh_matrices_1000.npz"
        self.article_lookup_map_path = "data/article_lookup_map.npy"

        self.dictionary = self.load_dictionary()
        self.search_matrix = sp.sparse.load_npz(self.search_matrix_path)
        self.SVD_search_matrix_US, self.SVD_search_matrix_Vh = np.load(self.search_matrix_SVD_pah).values()

        self.article_lookup_map = np.load(self.article_lookup_map_path)

    def load_dictionary(self):
        dictionary = {}
        with open(self.dictionary_path, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file):
                word, _ = line.strip().split(',')
                dictionary[word] = idx
        return dictionary


    def generate_search_vector(self, input):
        search_vector = np.zeros(len(self.dictionary))
        for word in input:
            if word in self.dictionary:
                search_vector[self.dictionary[word]] = 1

        search_vector = search_vector / np.linalg.norm(search_vector)
        return search_vector

    def search_articles(self, search_vector, max_results, method='SVD'):
        if method == 'SVD':
            US, Vh = self.SVD_search_matrix_US, self.SVD_search_matrix_Vh
            article_scores = US.dot(Vh.dot(search_vector))
        elif method == 'NORMAL':
            article_scores = self.search_matrix.dot(search_vector)

        relevant_indexes = np.where(article_scores != 0)[0]
        relevant_scores = article_scores[relevant_indexes]

        sorted_relevant_indexes = np.argsort(relevant_scores)[::-1]

        top_k_indexes = sorted_relevant_indexes[:max_results]
        top_k_article_indexes = relevant_indexes[top_k_indexes]

        top_articles = self.article_lookup_map[top_k_article_indexes]
        top_articles_similarity = relevant_scores[top_k_indexes]

        return zip(top_articles, top_articles_similarity)

    def search(self, input_string, method='NORMAL', max_results=10):
        print(f"SEARCHING FOR: {input_string}")
        sanitized_user_input = TextSanitizer.sanitize_text(input_string)
        search_vector = self.generate_search_vector(sanitized_user_input)

        search_result = self.search_articles(search_vector, max_results, method)
        return search_result


def print_result(search_result):
    for article_name, similarity in search_result:
        print(f"{similarity:.2f}\t{article_name}")

def main():
    SE = SearchEngine()
    while True:
        USER_INPUT = input(">")
        result = SE.search(USER_INPUT)
        print("method: default search")
        print_result(result)
        result = SE.search(USER_INPUT, method='SVD')
        print("method: noise removal with singular value decomposition")
        print_result(result)




if __name__ == "__main__":
    main()