import time
from .handling_useless_tokens import handling_useless_tokens
from .replace_abbreviations import replace_abbreviations_in_text
from .web_scrapping import scrap
from .cleaning import get_rid_html_tags
from .sentence_tokenization import tokenize_sentences
from .word_tokenization import tokenize_words
from .corrector import correct_words



async def pipeline_pln(route):
    print("a")
    # data scraping a
    start_time = time.time() 
    scraped_text = scrap(route)
    time_to_scrap = (time.time() - start_time) * 1000

    print(scraped_text)
    print(time_to_scrap)

    print("b")
    # cleaned words stiles b
    start_time = time.time()
    cleaned_text = get_rid_html_tags(scraped_text)
    time_to_clean_text = (time.time() - start_time) * 1000

    print(cleaned_text)
    print(time_to_clean_text)

    print("c")
    # tokenizing sentences and word tokens c
    start_time = time.time()
    tokenized_sentences = tokenize_sentences(cleaned_text)
    time_to_tokenize_sentences = (time.time() - start_time) * 1000

    start_time = time.time()
    tokenized_words = tokenize_words(tokenized_sentences)
    time_to_tokenize_words = (time.time() - start_time) * 1000

    print("b")
    # cleaned words b
    start_time = time.time()
    cleaned_tokens = handling_useless_tokens(tokenized_words)
    time_to_clean_tokens = (time.time() - start_time) * 1000
    
    print("d")
    # replaced abbreviations d
    start_time = time.time()
    replace_abbreviations = replace_abbreviations_in_text(cleaned_tokens)
    time_to_replace_abbreviations = (time.time() - start_time) * 1000

    print("e")
    # correct misspelled words e
    start_time = time.time()
    corrected_words = correct_words(replace_abbreviations)
    time_to_correct_words = (time.time() - start_time) * 1000

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
        },
        'cleaned_word_2': {
            'entry': tokenized_words,
            'exit': cleaned_tokens,
            'time': time_to_clean_tokens
        },
        'replaced_abbreviations': {
            'entry': cleaned_tokens,
            'exit': replace_abbreviations,
            'time': time_to_replace_abbreviations
        },
        'correct_words': {
            'entry': replace_abbreviations,
            'exit': corrected_words,
            'time': time_to_correct_words
        }
    }

    # print(data)
    return data