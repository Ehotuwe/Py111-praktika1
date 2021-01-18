from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    already_seen = []
    queue = [start_node]

    while queue:
        current_node = queue.pop ()
        already_seen.append (current_node)

        for node in g.neighbors (current_node):
            if node not in already_seen and node not in queue:
                queue.append (node)

    return already_seen
