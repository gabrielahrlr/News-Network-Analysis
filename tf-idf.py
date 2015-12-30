import numpy as np
import community
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from text_processing import *
from sklearn.cluster import AgglomerativeClustering, Ward
import networkx as nx
import matplotlib.pyplot as plt
from networkx import k_clique_communities
from networkx import shortest_path
from networkx import betweenness_centrality
import random
__author__ = 'Gabriela'


with open('espn_paper-text.json') as f:
    espn_dict = json.load(f)

#with open('fox_sports_nfl.json') as s:
 #   fox_nfl_dict = json.load(s)
#print(len(fox_nfl_dict))
with open('yahoo_paper.json') as f:
    yahoo_dict = json.load(f)

espn_dict.update(yahoo_dict)


print(len(espn_dict))

with open('espn_paper_sc_text.json') as f:
    espn_sc_dict = json.load(f)

espn_dict.update(espn_sc_dict)

print(len(espn_dict))
#
'''
counter = 0
values = []
key = {}

for k,v in espn_dict.items():
    values.append(v)
    key[k] = counter
    counter += 1
'''
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), tokenizer=clean_stopwords_lemmatize, stop_words='english')
tfs = tfidf.fit_transform(espn_dict.values())

#tfs = tfidf.fit_transform(fox_nfl_dict.values())

#tfs = tfidf.fit_transform(fox_fc_dict.values())

cs = cosine_similarity(tfs)
print(tfs)
print(cs)

cs[cs >= 1] = 0
cs[cs < 0.2] = 0
print(cs.shape)
D = nx.Graph(cs)
print(nx.number_of_edges(D))
remove = [node for node, degree in D.degree().items() if degree == 0]
D.remove_nodes_from(remove)
print(nx.number_of_nodes(D))
nx.draw(D)
plt.show()

r = lambda: random.randint(0,255)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#FF0099','#660066','#F4A460','#722f37','#37722f']
partition = community.best_partition(D)
print('=======>Partition', partition)
size = float(len(set(partition.values())))
pos = nx.spring_layout(D)
count = 0
for com in set(partition.values()):
    count += 1
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    color = '#%02X%02X%02X' % (r(),r(),r())
    nx.draw_networkx_nodes(D, pos, list_nodes, node_size=20,
                                node_color=color)


nx.draw_networkx_edges(D, pos)
plt.show()

#AgglomerativeClustering(n_clusters=10, linkage='average')
#nx.draw(D)
#plt.show()
clustering = AgglomerativeClustering(n_clusters=5,  affinity='euclidean', linkage='complete')
model = clustering.fit(cs)
plt.figure()
plt.show()
