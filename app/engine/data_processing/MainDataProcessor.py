import os

from ArticleLookupMapCreator import ArticleLookupMapCreator
from ArticleProcessor import ArticleProcessor
from ArticleVectorSVD import ArticleVectorSVD
from ArticleVectorizer import TextVectorizer
from DictionaryCreator import DictionaryCreator


class MainDataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path

    def run(self):
        self.process_articles()
        self.create_dictionary()
        self.create_article_lookup_map()
        self.vectorize_articles()
        self.compute_SVD()


    def process_articles(self):
        input_folder = os.path.join(self.data_path, "raw/raw_articles/")
        output_folder = os.path.join(self.data_path, "raw/sanitized_files/")
        article_processor = ArticleProcessor(input_folder, output_folder)
        article_processor.run()

    def create_dictionary(self):
        input_folder = os.path.join(self.data_path, "raw/sanitized_files/")
        output_file = os.path.join(self.data_path, "dictionary.txt")
        dictionary_creator = DictionaryCreator(input_folder, output_file)
        dictionary_creator.run()


    def create_article_lookup_map(self):
        input_folder = os.path.join(self.data_path, "raw/sanitized_files/")
        output_file = os.path.join(self.data_path, "article_lookup_map.npy")
        article_lookup_map_generator = ArticleLookupMapCreator(input_folder, output_file)
        article_lookup_map_generator.run()

    def vectorize_articles(self):
        dictionary_path = os.path.join(self.data_path, "dictionary.txt")
        input_folder = os.path.join(self.data_path, "raw/sanitized_files/")
        output_file = os.path.join(self.data_path, "term_by_document.npz")
        text_vectorizer = TextVectorizer(dictionary_path, input_folder, output_file)
        text_vectorizer.run()

    def compute_SVD(self):
        input_file = os.path.join(self.data_path, "term_by_document.npz")
        output_file = os.path.join(self.data_path, "US_Vh_matrices.npz")
        vector_decomposer = ArticleVectorSVD(input_file, output_file, 5000)
        vector_decomposer.run()


if __name__ == "__main__":
    MainDataProcessor("../data/").run()