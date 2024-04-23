import os
import time

import numpy as np
import scipy.sparse as sp


class TextVectorizer:
    def __init__(self, dictionary_path, input_folder, output_file):
        self.dictionary = self.load_dictionary(dictionary_path)
        self.input_folder = input_folder
        self.output_file = output_file
        self.start_time = time.time()
        self.total_files = 0
        self.processed_files = 0


    def run(self):
        self.total_files = len(os.listdir(self.input_folder))
        file_vectors = self.process_all_files()

        print("\nNormalizing document vectors...")
        processed_vectors = self.normalize_vectors(file_vectors)

        print("Saving processed vectors to file...")
        self.save_processed_vectors(processed_vectors)


    def process_all_files(self):
        file_vectors = []
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.input_folder, filename)
                file_vector = self.process_file(file_path)
                file_vectors.append(file_vector)
                self.processed_files += 1
                self.print_statistics()
        return sp.vstack(file_vectors)

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            vector = sp.dok_matrix((1, len(self.dictionary)), dtype=np.float64)
            for word in words:
                if word in self.dictionary:
                    index = self.dictionary[word]
                    vector[0, index] = vector.get((0, index), 0) + 1
        return vector.tocsr()


    def calculate_idf(self, file_vectors):
        N = file_vectors.shape[0]
        is_word_present = (file_vectors > 0)
        Nw = np.array(is_word_present.sum(axis=0))
        idf_values = np.log(N / Nw).flatten()
        return sp.diags(idf_values)

    def normalize_vectors(self, file_vectors):
        idf_diag = self.calculate_idf(file_vectors)

        file_vectors_idf = file_vectors.dot(idf_diag)

        row_norms = sp.linalg.norm(file_vectors_idf, axis=1)
        row_norms_inv = 1 / row_norms
        row_norms_inv_diag = sp.diags(row_norms_inv)

        return row_norms_inv_diag.dot(file_vectors_idf)

    def save_processed_vectors(self, processed_vectors):
        sp.save_npz(self.output_file, processed_vectors)

    def print_statistics(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        eta = 0
        if self.processed_files > 0:
            remaining_files = self.total_files - self.processed_files
            eta = remaining_files / self.processed_files * elapsed_time
        print(f"\rProcessed Files: {self.processed_files}/{self.total_files} | Elapsed Time: {elapsed_time:.2f} seconds | ETA: {eta:.2f} seconds", end="", flush=True)


    def load_dictionary(self, file_path):
        dictionary = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file):
                word, _ = line.strip().split(',')
                dictionary[word] = idx
        return dictionary


if __name__ == "__main__":
    dictionary_path = '../data/word_dictionary.txt'
    input_folder = '../data/raw/sanitized_files/'
    output_file = '../data/term_by_document.npz'
    text_vectorizer = TextVectorizer(dictionary_path, input_folder, output_file)
    text_vectorizer.run()
