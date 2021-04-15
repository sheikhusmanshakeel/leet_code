from collections import deque


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root):
    child_queue = deque()

    if root is None:
        return

    print(root.val)
