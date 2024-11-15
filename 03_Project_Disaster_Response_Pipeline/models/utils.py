import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import re

nltk.download(['punkt', 'punkt_tab', 'wordnet', 'averaged_perceptron_tagger'], quiet=True)

def tokenize(text):
    """Principal cleaning steps (substitute urls, normalization, delete unnecessary spaces),
    tokenization & lemmatization for a given text

    Args:
        text (str): text to preprocess 

    Returns:
        clean_tokens(list): clean word tokens for further preprocessing 
    """

    #replace all urls
    url_regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    #create tokens & lemmatize
    tokens = word_tokenize(text)
    
    #lemmatize, Normalize
    lemmatizer = WordNetLemmatizer()
        
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens