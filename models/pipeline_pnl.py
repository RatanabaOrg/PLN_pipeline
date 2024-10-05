import time
from .handling_useless_tokens import handling_useless_tokens
from .replace_abbreviations import replace_abbreviations_in_text
from .web_scrapping import scrap
from .cleaning import get_rid_html_tags
from .sentence_tokenization import tokenize_sentences
from .word_tokenization import tokenize_words



async def pipeline_pln(route):
    # data scraping a
    start_time = time.time() 
    scraped_text = scrap(route)
    time_to_scrap = (time.time() - start_time) * 1000

    # cleaned words stiles b
    start_time = time.time()
    cleaned_text = get_rid_html_tags(scraped_text)
    time_to_clean_text = (time.time() - start_time) * 1000

    # tokenizing sentences and word tokens c
    start_time = time.time()
    tokenized_sentences = tokenize_sentences(cleaned_text)
    time_to_tokenize_sentences = (time.time() - start_time) * 1000

    start_time = time.time()
    tokenized_words = tokenize_words(tokenized_sentences)
    time_to_tokenize_words = (time.time() - start_time) * 1000

    # cleaned words b
    start_time = time.time()
    cleaned_tokens = handling_useless_tokens(tokenized_words)
    time_to_clean_tokens = (time.time() - start_time) * 1000
    
    # replaced abbreviations d
    start_time = time.time()
    replace_abbreviations = replace_abbreviations_in_text(cleaned_tokens)
    time_to_clean_tokens = (time.time() - start_time) * 1000

    # correct misspelled words e

    data = {
        'scraping': {
            'entry': route,
            'exit': scraped_text,
            'time': time_to_scrap
        },
        'cleaned_word_1': {
            'entry': time_to_scrap,
            'exit': cleaned_text,
            'time': time_to_clean_text
        },
        'tokenized_sentences': {
            'entry': cleaned_text,
            'exit': tokenized_sentences,
            'time': time_to_tokenize_sentences
        },
        'tokenized_words': {
            'entry': tokenized_sentences,
            'exit': tokenized_words,
            'time': time_to_tokenize_words
        }
    }
    return data