from models.handling_useless_tokens import handling_useless_tokens
from models.replace_abbreviations import replace_abbreviations_in_text

# data scraping a

# cleaned words stiles b

# tokenizing sentences and word tokens c
word_tokens_en = ['I\'m', 'heading', 'to', 'the', 'gym', 'ASAP', ',', 'but', 'I\'ll', 'be', 'back', 'before', '5', 'PM', '.', 'FYI', ',', 'I\'ll', 'grab', 'some', 'food', 'on', 'the', 'way']

# cleaned words b
cleaned_words = handling_useless_tokens(word_tokens_en)
print(cleaned_words)

# replaced abbreviations d
replace_abbreviations = replace_abbreviations_in_text(cleaned_words)
print(replace_abbreviations)

# correct misspelled words e