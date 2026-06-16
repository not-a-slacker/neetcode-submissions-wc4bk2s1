# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node==None:
                return [0,0]
            t = depth(node.right)
            a = t[0]
            d1 = t[1]
            t = depth(node.left)
            b = t[0]
            d2 = t[1]
            diameter = max([d1,d2, a+b+1])
            return [(max(a,b) + 1),diameter]
        depth,diameter = depth(root)
        return diameter - 1


        