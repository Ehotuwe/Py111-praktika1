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
    dfs_list = []
    queue = [start_node]

    while queue:
        current_node = queue.pop()
        if current_node not in already_seen:
            already_seen.append(current_node)
            dfs_list.append(current_node)
            queue.extend(reversed(list(g.neighbors (current_node))))

    return dfs_list
