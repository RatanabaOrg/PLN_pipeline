import re

def handling_useless_tokens(sentences):
    cleaned_words = []
    for sentence in sentences:
        cleaned_sentence = []  
        for word in sentence:
            cleaned_word = re.sub(r'[^\w\s]', '', word).lower()  
            if cleaned_word:  
                cleaned_sentence.append(cleaned_word)  
        cleaned_words.append(cleaned_sentence)  
    return cleaned_words