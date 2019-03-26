# https://leetcode.com/problems/sum-of-left-leaves/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0

    def sum_func(self, node):

        def sum_left_leaves(node):
            if node is not None:
                if node.left is not None and node.left.left is None and node.left.right is None:
                    self.sum += node.left.val
                sum_left_leaves(node.left)
                sum_left_leaves(node.right)

        sum_left_leaves(node)
        return self.sum

    def sum_func2(self, node):

        def sum_left_leaves(node):
            if node:
                if node.left and not node.left.left and not node.left.right:
                    self.sum += node.left.val
                sum_left_leaves(node.left)
                sum_left_leaves(node.right)

        sum_left_leaves(node)
        return self.sum


n1 = TreeNode(7)
n1.left = TreeNode(5)
n1.right = TreeNode(8)
n1.left.left = TreeNode(10)
n1.left.right = TreeNode(15)
n1.right.left = TreeNode(9)
n1.right.right = TreeNode(6)
n1.right.right.left = TreeNode(1)

print(Solution().sum_func2(n1))
print(Solution().sum_func(n1))
