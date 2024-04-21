import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# nltk.download('stopwords')
# nltk.download('punkt')

class TextSanitizer:
    @staticmethod
    def sanitize_text(text):
        tokens = word_tokenize(text)
        tokens = TextSanitizer.remove_stop_words(tokens)
        tokens = TextSanitizer.remove_punctuation(tokens)
        tokens = TextSanitizer.stem_words(tokens)
        return tokens

    @staticmethod
    def remove_stop_words(tokens):
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        return filtered_tokens

    @staticmethod
    def remove_punctuation(tokens):
        table = str.maketrans('', '', string.punctuation)
        stripped = [token.translate(table) for token in tokens]
        return [token for token in stripped if token]

    @staticmethod
    def stem_words(tokens):
        ps = PorterStemmer()
        stemmed_tokens = [ps.stem(token) for token in tokens]
        return stemmed_tokens