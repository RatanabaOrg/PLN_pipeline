import nltk
from nltk.data import find
try:
    find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
from nltk.tokenize import word_tokenize


def tokenize_words(sentences):
    all_tokens = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        all_tokens.append(words)
    return all_tokens

# url = "https://www.amazon.co.uk/dp/B0CGVTJ583/ref=sspa_dk_detail_4?pd_rd_i=B0CGVTJ583&pd_rd_w=j8DH0&content-id=amzn1.sym.6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_p=6910e71b-a457-4d1b-9885-9ac6dea34603&pf_rd_r=TD9BS15D1F72TTW87YB5&pd_rd_wg=aOTnF&pd_rd_r=1d4023ee-f894-487e-a3a7-2fbc25172bd0&s=electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy&th=1"
# tokens = tolkenize_words(tolkenize_sentences(get_rid_html_tags(scrap(url))))

# for i, words in enumerate(tokens):
#     print(f"Sentence #{i+1}:")
#     print(words)
#     print()