from models.handling_useless_tokens import handling_useless_tokens

word_tokens_en = ['The', 'product', 'is', 'good', ',', 'but', 'it', 'has', 'some', 'flaws']

# cleaned_words 
cleaned_words = handling_useless_tokens(word_tokens_en)
print(cleaned_words)