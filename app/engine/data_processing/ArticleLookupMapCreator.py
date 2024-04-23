import os

import numpy as np


class ArticleLookupMapCreator:
    def __init__(self, input_folder, output_file):
        self.input_folder = input_folder
        self.output_file = output_file

    def run(self):
        self.generate_article_lookup_map()

    def generate_article_lookup_map(self):
        filenames = []
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".txt"):
                filenames.append(filename[:-4])  # removes .txt

        filenames = np.array(filenames)
        np.save(self.output_file, filenames)


if __name__ == "__main__":
    input_folder = "../data/raw/sanitized_files"
    output_file = "../data/article_lookup_map.npy"
    article_lookup_map_generator = ArticleLookupMapCreator(input_folder, output_file)
    article_lookup_map_generator.run()
