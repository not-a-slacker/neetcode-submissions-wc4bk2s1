# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        a = self.lowestCommonAncestor(root.right,p,q)
        b = self.lowestCommonAncestor(root.left,p,q)
        if not a and not b:
            if root.val==p.val or root.val==q.val:
                return root
            return None
        if a and a.val!= p.val and a.val!=q.val:
            return a
        if b and b.val!= p.val and b.val!= q.val:
            return b
        l = -101
        r = -101
        if a:
            r = a.val
        if b:
            l = b.val
        if r==p.val and l == q.val:
            return root
        if r==q.val and l == p.val:
            return root
        if r == p.val or r==q.val:
            if root.val == p.val or root.val == q.val:
                return root
            return a
        if l == q.val or l == p.val:
            if root.val == p.val or root.val == q.val:
                return root
            return b
        
        
        
        


        