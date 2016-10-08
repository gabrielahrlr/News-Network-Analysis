import networkx as nx
__author__ = 'Gabriela & Maira'

def get_shortest_path_average_len(g):
    """
    returns the average shortest path length of a graph
    :param g: ER or WS graph
    :return: average shortest path len
    """
    sps = nx.shortest_path_length(g)
    paths_size = 0
    for n0 in sps.values():
        for n1 in n0.values():
            paths_size += n1
    n_nodes = g.number_of_nodes()
    return paths_size/float(n_nodes*(n_nodes-1))


def get_clustering_coefficient(g):
    """
    returns the clustering coefficient of a graph
    :param g: ER or WS graph
    :return: clustering coefficient path len
    """
    return nx.average_clustering(g)


def get_average_degree(g):
    """
    returns the average degree of a graph
    :param g: Undirected graph
    :return: average degree of a graph
    """
    n, k = g.order(), g.size()
    avg_deg = float(k) / n
    return avg_deg