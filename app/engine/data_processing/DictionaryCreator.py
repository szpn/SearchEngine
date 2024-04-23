import concurrent.futures
import os
import time
from collections import defaultdict


class DictionaryCreator:
    def __init__(self, input_folder, output_file):
        self.input_folder = input_folder
        self.output_file = output_file
        self.word_counts = defaultdict(int)
        self.start_time = time.time()
        self.total_files = 0


    def word_filter(self, word, count):
        return count > 15 and len(word) > 1

    def run(self):
        self.process_all_files()
        self.save_dictionary()


    def process_all_files(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_file, filename) for filename in os.listdir(self.input_folder)]
            self.total_files = len(futures)

            processed_files = 0
            for future in concurrent.futures.as_completed(futures):
                processed_files += 1
                self.print_statistics(processed_files)


    def process_file(self, filename):
        if filename.endswith(".txt"):
            file_path = os.path.join(self.input_folder, filename)
            word_counts_partial = self.extract_words_from_file(file_path)
            self.update_dictionary(word_counts_partial)


    def extract_words_from_file(self, file_path):
        word_counts = defaultdict(int)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_words = line.strip().split()
                for word in line_words:
                    word_counts[word] += 1
        return word_counts

    def update_dictionary(self, word_counts_partial):
        for word, count in word_counts_partial.items():
            self.word_counts[word] += count



    def save_dictionary(self):
        sorted_word_counts = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        with open(self.output_file, 'w', encoding='utf-8') as output:
            for word, count in sorted_word_counts:
                if self.word_filter(word, count):
                    output.write(f"{word},{count}\n")


    def print_statistics(self, processed_files):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        remaining_files = self.total_files - processed_files
        eta = remaining_files / processed_files * elapsed_time if processed_files > 0 else float('inf')
        print(f"\rProcessed Files: {processed_files}/{self.total_files} | Elapsed Time: {elapsed_time:.2f} seconds | ETA: {eta:.2f} seconds", end="", flush=True)


if __name__ == "__main__":
    input_folder = "../data/raw/sanitized_files"
    output_file = "../data/word_dictionary.txt"
    word_counter = DictionaryCreator(input_folder, output_file)
    word_counter.run()
