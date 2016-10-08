from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Network_Analysis import *
import json
from text_processing import *
import networkx as nx
import matplotlib.pyplot as plt
__author__ = 'Gabriela & Maira'


def get_tf_idf(values):
    """
    returns a matrix, with n rows where n is the number of docs and
    m columns where m is the number of words, and each row represent
    the tf-idf vector for the article nth.
    :param values: The tokenized and cleaned words for each doc or article.
    :return tfidfs: A n x m matrix
    """
    tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), tokenizer=clean_stopwords_lemmatize,
                            stop_words='english',token_pattern=u'\w{3,}')
    tfidfs = tfidf.fit_transform(values)
    return tfidfs


def get_cosine_similarity(tfidfs):
    """
    returns a list of tokens with no stop , no punctuation and stemmed
    :param title: Raw title of an article
    :return: a list of lemmatized-cleaned tokens
    """
    cs = cosine_similarity(tfidfs)
    return cs