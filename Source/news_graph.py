import networkx as nx
from Network_Analysis import *
import matplotlib.pyplot as plt
__author__ = 'Gabriela & Maira'

def get_network(cs, threshold):
    """
    returns a networkx Graph.
    :param cs: The cosine similarity matrix of the docs or articles
    :return G: A networkx graph
    """
    cs[cs >= 1] = 0
    cs[cs < threshold] = 0
    print(cs.shape)
    G = nx.Graph(cs)
    remove = [node for node, degree in G.degree().items() if degree <= 3]
    G.remove_nodes_from(remove)
    print(nx.number_of_nodes(G))
    print(nx.number_of_edges(G))
    print(get_shortest_path_average_len(G))
    print(get_clustering_coefficient(G))
    print(get_average_degree(G))
    nx.draw(G, node_size=30, with_labels=False)
    plt.show()
    return G