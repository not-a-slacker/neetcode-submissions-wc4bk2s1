# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        a = self.isSameTree(root.right,subRoot.right)
        b = self.isSameTree(root.left,subRoot.left)
        return (a and b)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            a = self.isSameTree(root.right,subRoot.right)
            b = self.isSameTree(root.left,subRoot.left)
            if a and b:
                return True
            else:
                False
        c = self.isSubtree(root.right,subRoot)
        d = self.isSubtree(root.left,subRoot)
        
        return (c or d)


        