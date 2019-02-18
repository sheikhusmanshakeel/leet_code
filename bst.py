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
        while(current != None):
            previous = current
            if val < current.val:
                current = current.left
            else:
                current = current.right
        
        if previous == None:
            self.root = TreeNode(val)
            return

        if (val <  previous.val ):
            previous.left = TreeNode(val)
        else:
            previous.right = TreeNode(val)

    def insert_recur(self, root, val):
        if root == None:
            root = TreeNode(val)
        else:
            if root.val  < val:
                if root.right == None:
                    root.right = TreeNode(val)
                else:
                    self.insert_recur(root.right, val)
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                else:
                    self.insert_recur(root.left, val)







        

        

