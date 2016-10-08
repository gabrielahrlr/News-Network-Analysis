import newspaper
import json
from newspaper import Config
from text_processing import *
from collections import Counter

__author__ = 'Gabriela & Maira'

#  Important Newspapers' Links
'''
# ====== NEWSPAPERS to dump ================================

# ============ Wall Street Journal Newspaper - Markets section ====================================
wsj_paper = newspaper.build('http://www.wsj.com/', language='en', memoize_articles=False)

# ============ CNN Newspaper - Money section =======================================================
cnn_paper = newspaper.build('http://edition.cnn.com/', language='en', fetch_images=False, memoize_articles=False)

# =========== New York Times - Business section ====================================================
nyt_paper = newspaper.build('http://www.nytimes.com/', config=config)

# ========== USA Today - Money section ===================================
usa_paper = newspaper.build('http://www.usatoday.com/', config=config)

# ========== ESPN ===========================
espn_paper = newspaper.build('http://espn.go.com/', config=config)
espn_paper = newspaper.build('http://www.espnfc.com/', config=config)

# ========== Fox Sports ========
fox_paper = newspaper.build('http://www.foxsports.com/soccer', config=config)
fox_paper = newspaper.build('http://www.foxsports.com/', config=config)


# ========= Yahoo Sports ==========
yahoo_paper = newspaper.build('http://sports.yahoo.com/', config=config)
yahoo_news = newspaper.build('http://news.yahoo.com/', config=config)


# ========= Sporting News ======
sporting_paper = newspaper.build('http://www.sportingnews.com/', config=config)

# Check how many articles we are downloading

# ======== NBC News ========
nbc_news = newspaper.build('http://www.nbcnews.com', config=config)
'''


def get_newspaper_articles(link, file_name):
    """
    returns two dictionaries, one (d) containing as keys the titles of the
    articles and as values the full text. The other one (d_tok), contains as
    keys the articles id followed by the most common word in this article
    and as values the text already preprocessed (stop words removal,
    punctuation removal and lemmatizing)
    These two dictionaries are saved as json files, in order to
    be able to access to this information later, without downloading all the
    articles again.
    :param link: The link of the newspaper website
    :param file_name: The name of the files to be saved as .json format. For
                      the first dictionary it will take the name as file_name,
                      for the second one it will include 'tok'.
    :return d, d_tok: dictionaries containing the information of each article.

    Example:
            get_newspaper_articles('http://www.foxsports.com/', 'fox_test')
    """
    config = Config()
    config.memoize_articles = False
    config.MIN_WORD_COUNT = 100
    config.fetch_images = False
    config.language = 'en'
    paper_built = newspaper.build(link, config=config)
    print('This new paper contains: ', paper_built.size(), ' articles')
    name_dtok = file_name + '_' + 'tok.json'
    name_d = file_name + '.json'
    d = {}
    d_tok = {}
    i = 0
    for article in paper_built.articles:
        try:
            article.download()
        except Exception:
            continue
        try:
            article.parse()
        except Exception:
            continue
        try:
            article.nlp()
        except:
            continue
        if article.is_valid_body():
            d[article.title] = article.text
            text = clean_stopwords_lemmatize(article.text)
            text.extend(clean_title(article.title))
            id = Counter(text)
            ids = id.most_common(1)
            doc_id = 'doc_' + str(i) + '_'+ids[0][0]
            print(doc_id, '---->', article.title)
            d_tok[doc_id] = text
            i += 1
        else:
            continue
            
    with open(name_d, 'w') as f:
        json.dump(d, f)

    with open(name_dtok, 'w') as f:
        json.dump(d_tok, f)

    return d, d_tok
