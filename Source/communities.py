import networkx as nx
import random
import community
import matplotlib.pyplot as plt
__author__ = 'Gabriela'


# "Louvain" Modularity Optimization Method
def get_community_best_partition(G, nodes_labels=False):
    partition = community.best_partition(G)
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    r = lambda: random.randint(0,255)
    count = 0
    print('Number of partitions: ', size)
    for com in set(partition.values()):
        count += 1
        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
        color = '#%02X%02X%02X' % (r(), r(), r())
        labels = dict(zip(list_nodes, list_nodes))
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=100,
                               node_color=color, with_labels=False)
        if nodes_labels:
            nx.draw_networkx_labels(G, pos, labels, font_size=5)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()
    return partition


