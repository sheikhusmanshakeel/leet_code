import numpy as np
from collections import deque


class Node:
    def __init__(self, id, color, dist, parent=None, adj=None):
        self.id = id
        self.color = color
        self.dist = dist
        self.adj = adj
        self.parent = parent


def dfs_search(source):
    if source is None or source.color == 1:
        return
    else:
        print(source.id)
        source.color = 1
        if source.adj is not None:
            for n in source.adj:
                if n.color == 0:
                    dfs_search(n)

    return


def bfs_search(source):
    source.color = 1
    print(source.id)
    node_queue = deque()
    if source.adj is not None:
        node_queue.append(source)
        while node_queue.__len__() > 0:
            node = node_queue.popleft()
            if node.adj is not None:
                for n in node.adj:
                    if n.color == 0:
                        n.color = 1
                        print(n.id)
                        node_queue.append(n)

    else:
        return


def route(source, end):
    has_path = False
    node_queue = deque()
    source.color = 1  # means that the node has been visited
    node_queue.append(source)
    while node_queue.__len__() > 0 and not has_path:
        node = node_queue.popleft()
        if node.adj is not None:
            for n in node.adj:
                if n.id == end.id:
                    has_path = True
                    break
                else:
                    n.color = 1
                    node_queue.append(n)

    return has_path



node1 = Node(1, 0, np.nan)
node2 = Node(2, 0, np.nan)
node3 = Node(3, 0, np.nan)
node4 = Node(4, 0, np.nan)
node5 = Node(5, 0, np.nan)
node6 = Node(6, 0, np.nan)
node7 = Node(7, 0, np.nan)
node1.adj = [node2, node4, node7]
node4.adj = [node3, node5]
node5.adj = [node6]
node6.adj = [node2]

# dfs_search(node1)
# bfs_search(node4)
val = route(node1, node6)
print(val)