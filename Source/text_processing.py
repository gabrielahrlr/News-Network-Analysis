import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
__author__ = 'Gabriela & Maira'


# Tokenization
def tokenize(text):
    """
    returns a list of tokens with no punctuation
    :param text: Raw text
    :return: a list of tokens
    """
    lowers = text.lower()
    trans = {ord(c): None for c in string.punctuation}
    no_punctuation = lowers.translate(trans)
    trans_dig = {ord(c): None for c in string.digits}
    no_digits = no_punctuation.translate(trans_dig)
    tokens = nltk.word_tokenize(no_digits)
    return tokens


# Stop Words removal
def stopwordsRem(tokens):
    """
    returns a list of tokens with no stop words
    :param tokens: A list of tokens
    :return: a list of tokens with no stop words
    """
    no_sw = [t for t in tokens if not t in stopwords.words('english')]
    return no_sw


# Porter Stemer
def stemmerP(tokens, stemmer):
    """
    returns a list of stemmed tokens
    :param tokens: A list of tokens
    :param stemmer: the stemmer method to be applied
    :return: a list of stemmed tokens
    """
    stemmed =[]
    for token in tokens:
        stemmed.append(stemmer.stem(token))
    return stemmed


# Lemmatizing
def lemmatize_tokens(tokens):
    """
    returns a list of lemmatized tokens
    :param tokens: A list of tokens
    :return: a list of lemmatized tokens
    """
    lemmatized = []
    wordnet_lemmatizer = WordNetLemmatizer()
    for token in tokens:
        lemmatized.append(wordnet_lemmatizer.lemmatize(token, pos='v'))
    return lemmatized


# Clean text with non stop words and  non punctuation, return tokens
def clean_stopwords(text):
    """
    returns a list of tokens with no stop words and no punctuation
    :param text: Raw text
    :return: a list of cleanned tokens
    """
    tokens = tokenize(text)
    tokens = stopwordsRem(tokens)
    return tokens


# Clean text with no stop words, no punctuation, stemming, return tokens
def clean_stopwords_stemming(text):
    """
    returns a list of tokens with no stop , no punctuation and stemmed
    :param text: Raw text
    :return: a list of stemmed-cleaned tokens
    """
    tokens = clean_stopwords(text)
    stemmer = PorterStemmer()
    tokens = stemmerP(tokens, stemmer)
    return tokens


def clean_stopwords_lemmatize(text):
    """
    returns a list of tokens with no stop , no punctuation and lemmatized
    :param text: Raw text
    :return: a list of lemmatized-cleaned tokens
    """
    tokens = clean_stopwords(text)
    tokens = lemmatize_tokens(tokens)
   # count = Counter(tokens)
   # c = count.most_common(15)
   # b = [str(i[0]) for i in c]
   # keywords = [t for t in tokens if t in b]
    news = ['ESPN', 'espn', 'foxsports', 'fox', 'cnn', 'yahoo', '•', '-', '●']
    keywords = [k for k in tokens if not k in news]
    return keywords


def clean_title(title):
    """
    returns a list of tokens with no stop , no punctuation and stemmed
    :param title: Raw title of an article
    :return: a list of lemmatized-cleaned tokens
    """
    tokens = clean_stopwords(title)
    tokens = lemmatize_tokens(tokens)
    return tokens


# Clean text with no stop words, no punctuation and non dict words, return tokens
# Remove dictionary words It requires enchant library.
'''
def rem_dict_words(tokens):
    d = enchant.Dict("en_US")
    no_dict = []
    for token in tokens:
        if not d.check(token):
            no_dict.append(token)
    return no_dict
'''

'''
def clean_stopwords_non_dict(text):
    tokens = clean_stopwords(text)
    tokens = rem_dict_words(tokens)
    return tokens

'''