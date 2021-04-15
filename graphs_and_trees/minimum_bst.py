class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def create_minimum_bst(a, start, end, l):
    if end < start:
        return None

    mid = int((start + end) / 2)
    if mid >= l:
        return None
    root = Node(a[mid])
    root.left = create_minimum_bst(a, start, mid - 1, l)
    root.right = create_minimum_bst(a, mid + 1, end, l)
    return root


input1 = [1, 2, 3, 4, 5, 6, 7, 8]
output1 = create_minimum_bst(input1, 0, len(input1), len(input1))
print(output1)
