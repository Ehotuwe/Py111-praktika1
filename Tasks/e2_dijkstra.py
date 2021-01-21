from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    l = list (g)
    d = {k: float ('inf') for k in l}
    d[starting_node] = 0
    neighbors = []
    queue = [starting_node]

    while queue:
        current_node = queue.pop ()
        neighbors.append (current_node)
        for node in g.neighbors (current_node):
            if node not in neighbors and node not in queue:
                queue.append (node)

            if d[node] > g[current_node][node]['weight'] + d[current_node]:
                d[node] = g[current_node][node]['weight'] + d[current_node]

    return d