import re
import nltk
nltk.data.path.append('C:\\path\\to\\your\\desired\\nltk_data')
nltk.download('punkt')
nltk.download('punkt_tab')

def tokenize_sentences(text):
    default_sentence_tokenizer = nltk.sent_tokenize
    fixed_text = re.sub(r"(?<!\s)(\.)([A-Z])", r"\1 \2", text)
    basic_sentence_tokens_en = default_sentence_tokenizer(text=fixed_text)
    return basic_sentence_tokens_en
