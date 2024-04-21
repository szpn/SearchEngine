import os
import concurrent.futures
import time

from TextSanitizer import TextSanitizer


class ArticleProcessor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.saved_topics_count = 0
        self.total_files = 0
        self.start_time = time.time()


    def run(self):
        self.total_files = len(os.listdir(self.input_folder))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_file, os.path.join(self.input_folder, filename)) for filename in os.listdir(self.input_folder) if filename.endswith(".txt")]
            concurrent.futures.wait(futures)

    def process_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        content = self.remove_end(content)

        sanitized_text = TextSanitizer.sanitize_text(content)

        if len(sanitized_text) == 0:
            return

        filename = os.path.basename(filepath)
        self.save_file(sanitized_text, filename)
        self.print_statistics()

    def remove_end(self, text):
        references_index = text.find("== References ==")
        websites_index = text.find("== Other websites ==")

        if references_index != -1:
            text = text[:references_index]
        if websites_index != -1:
            text = text[:websites_index]

        return text

    def save_file(self, tokens, filename):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        with open(os.path.join(self.output_folder, filename), 'w', encoding='utf-8') as file:
            file.write(' '.join(tokens))
        self.saved_topics_count += 1


    def print_statistics(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        processed_files = self.saved_topics_count
        files_per_second = processed_files / elapsed_time
        remaining_files = self.total_files - processed_files
        eta = remaining_files / files_per_second if files_per_second > 0 else float('inf')
        print(f"\rProcessed Files: {processed_files}/{self.total_files} | Elapsed Time: {elapsed_time:.2f} seconds | ETA: {eta:.2f} seconds", end="", flush=True)



if __name__ == "__main__":
    input_folder = "../data/raw/raw_articles"
    output_folder = "../data/raw/sanitized_files"
    text_processor = ArticleProcessor(input_folder, output_folder)
    text_processor.run()
