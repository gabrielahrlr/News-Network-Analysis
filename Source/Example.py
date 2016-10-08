from tfidf_cosine import *
from news_graph import *
from communities import *

__author__ = 'Gabriela & Maira'

# ======== Network 1 ===================
with open('cnn_text.json') as f:
    docs_dict = json.load(f)

with open('usa_text.json') as f:
    usa_dict = json.load(f)

docs_dict.update(usa_dict)

with open('nbc_text.json') as f:
    nbc_dict = json.load(f)
docs_dict.update(nbc_dict)

with open('huff_post.json') as f:
    huff_dict = json.load(f)

docs_dict.update(huff_dict)

# ======== Network 2 ===================
'''
with open('cnn_text.json') as f:
    docs_dict = json.load(f)

with open('huff_post.json') as f:
    huff_dict = json.load(f)

docs_dict.update(huff_dict)
'''

# ======== Network 3 ===================
''''
with open('espn_paper-text.json') as f:
    docs_dict = json.load(f)

with open('yahoo_paper.json') as f:
    yahoo_dict = json.load(f)

docs_dict.update(yahoo_dict)

with open('fox_sc_text.json') as f:
    fox_sc_dict = json.load(f)

docs_dict.update(fox_sc_dict)
'''''

print('final len',len(docs_dict))


with open('Network1-news.json', 'w') as f:
    json.dump(docs_dict, f)


counter = 0
values = []
docs = {}

for k, v in docs_dict.items():
    values.append(v)
    docs[counter] = k
    counter += 1

print(docs)

with open('Network1-ids-titles.json', 'w') as f:
    json.dump(docs, f)

tfidfs = get_tf_idf(values)
cs = get_cosine_similarity(tfidfs)

G = get_network(cs, 0.25)

Partitions = get_community_best_partition(G, nodes_labels=True)
