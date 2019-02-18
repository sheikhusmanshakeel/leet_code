# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def inorder_traversal( root, L, R):
            if root != None:
                inorder_traversal(root.left,L,R)
                if (L <= root.val) and (R >= root.val):
                    self.output += root.val
                inorder_traversal(root.right,L,R)
        self.output = 0
        inorder_traversal(root,L,R)
        return self.output


 

# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
# root.right.right = TreeNode(18)
# print(Solution().rangeSumBST(root,7,15))
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
root.left.left.left = TreeNode(1)
root.left.right.left = TreeNode(6)
print(Solution().rangeSumBST(root,6,10))
