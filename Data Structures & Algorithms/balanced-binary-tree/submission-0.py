# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root==None:
                return (0,True)
            a,b = dfs(root.right)
            c,d = dfs(root.left)
            if b and d:
                if abs(a-c) <=1 :
                    return (max(a,c) + 1,True)
                else:
                    return (max(a,c)+1,False)
            else:
                return (max(a,c)+1,False)
        a,b = dfs(root)
        return b

        