import os

class DescriptionExtractor:
    def __init__(self):
        module_dir = os.path.dirname(os.path.abspath(__file__))
        self.base_path = module_dir
        self.articles_path = os.path.join(module_dir, 'data', 'raw', 'raw_articles')

    def get_description(self, article_name, max_length=200):
        article_path = os.path.join(self.articles_path, article_name + '.txt')
        description = ""
        description_length = 0
        with open(article_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("==") or description_length >= max_length:
                    break
                description += line
                description_length += len(line)

        return description