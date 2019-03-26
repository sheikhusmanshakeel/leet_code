# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def insert(self, val):
        current = self.root
        previous = None
        while current is not None:
            previous = current
            if val < current.val:
                current = current.left
            else:
                current = current.right

        if previous is None:
            self.root = TreeNode(val)
            return

        if val < previous.val:
            previous.left = TreeNode(val)
        else:
            previous.right = TreeNode(val)

    def insert_recur(self, root, val):
        if root is None:
            root = TreeNode(val)
        else:
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insert_recur(root.right, val)
            else:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insert_recur(root.left, val)


def inorderTraversal(root):
    l = []

    def inorder_traversal(root):
        if root is not None:
            inorder_traversal(root.left)
            l.append(root.val)
            inorder_traversal(root.right)

    inorder_traversal(root)
    return l


def preorderTraversal(root):
    l = []

    def preorder_traversal(root):
        if root is not None:
            l.append(root.val)
            preorder_traversal(root.left)
            preorder_traversal(root.right)

    preorder_traversal(root)
    return l


def combine_traversal(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    root1.val += root2.val
    root1.left = combine_traversal(root1.left, root2.left)
    root1.right = combine_traversal(root1.right, root2.right)
    return root1


def combine_traversal2(root1, root2):
    if root1 is None:
        return root2
    if root2 is None:
        return root1
    root1.left = combine_traversal2(root1.left, root2.left)
    root1.val += root2.val
    root1.right = combine_traversal2(root1.right, root2.right)
    return root1


def maxDepth(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree 
        v = node.val
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        # Use the larger one 
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1


t = Tree(5)
t.insert(2)
t.insert(3)
t.insert(7)
t.insert(6)
t.insert(10)
t.insert(1)
print(inorderTraversal(t.root))
print(preorderTraversal(t.root))
# t = Tree(15)
# t.insert(10)
# t.insert(5)
# t.insert(11)
# t.insert(12)
# t.insert(13)
# t.insert(20)

# print(maxDepth(t.root))

# u = Tree(5)
# u.insert(4)
# u.insert(6)

# x = combine_traversal2(t.root,u.root)
# inorder_traversal(x)
