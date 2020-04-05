import numpy as np
from collections import deque


class GNode:
    def __init__(self, id, color, dist, parent=None, adj=None):
        self.id = id
        self.color = color
        self.dist = dist
        self.adj = adj
        self.parent = parent


def BFS(graph, source):
    source.color = 1
    source.dist = 0
    q = deque()
    q.append(source)
    while 0 < q.__len__():
        u = q.popleft()
        for v in u.adj:
            if v.color == 0:
                v.color = 1
                v.dist = u.dist + 1
                v.parent = u
                q.append(v)
        u.color = 2


node1 = GNode(1, 0, np.nan)
node2 = GNode(2, 0, np.nan)
node3 = GNode(3, 0, np.nan)
node4 = GNode(4, 0, np.nan)
node5 = GNode(5, 0, np.nan)
node6 = GNode(6, 0, np.nan)
node1.adj = [node2, node4]
node2.adj = [node5]
node3.adj = [node6, node5]
node4.adj = [node2]
node5.adj = [node4]
node6.adj = [node6]
node1.adj = [node2]

g = {2: node2, 3: node3, 4: node4, 5: node5, 6: node6}
BFS(g, node1)
