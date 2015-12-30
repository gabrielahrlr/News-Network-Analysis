import newspaper
import json
from newspaper import Config
from text_processing import *
from collections import Counter

__author__ = 'Gabriela'

config = Config()
config.memoize_articles = False
config.MIN_WORD_COUNT = 60
config.fetch_images = False
config.language = 'en'

# ====== NEWSPAPERS to dump ================================

# ============ Wall Street Journal Newspaper - Markets section ====================================
#wsj_paper = newspaper.build('http://www.wsj.com/news/us', language='en', memoize_articles=False)

# ============ CNN Newspaper - Money section =======================================================
#cnn_paper = newspaper.build('http://money.cnn.com/', language='en', fetch_images=False, memoize_articles=False)

# =========== New York Times - Business section ====================================================
#nyt_paper = newspaper.build('http://www.nytimes.com/pages/business/index.html', config=config)

# ========== USA Today - Money section ===================================
#usa_paper = newspaper.build('http://www.usatoday.com/money/', config=config)

# ========== ESPN ===========================
#espn_paper = newspaper.build('http://espn.go.com/', config=config)
#espn_paper = newspaper.build('http://www.espnfc.com/', config=config)

# ========== Fox Sports ========
#fox_paper = newspaper.build('http://www.foxsports.com/', config=config)
#fox_paper = newspaper.build('http://www.foxsports.com/nfl', config=config)
#fox_paper = newspaper.build('http://www.espnfc.com/', config=config)

# ========= Yahoo Sports ==========
#yahoo_paper = newspaper.build('http://sports.yahoo.com/', config=config)

# ========= Sporting News ======
sporting_paper = newspaper.build('http://www.sportingnews.com/', config=config)
# Check how many articles we are downloading
print(sporting_paper.size())

d = {}
d_tok = {}
i = 0
for article in sporting_paper.articles:
    try:
        article.download()
    except Exception:
        continue
    try:
        article.parse()
    except Exception:
        continue
    article.nlp()
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


with open('sporting_text.json', 'w') as f:
    json.dump(d, f)

with open('sporting_tokens.json', 'w') as f:
    json.dump(d_tok, f)