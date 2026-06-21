# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,minv,maxv):
            print(f"root.val : {root.val} ; minv : {minv} ; maxv : {maxv}")
            if not root:
                return True
            a = True
            if root.val <= minv or root.val >= maxv:
                a = False
                return a
            if root.left:
                if root.left.val >= root.val:
                    a = False
                    return a
                l_maxv = min(maxv,root.val)
                if not dfs(root.left,minv,l_maxv):
                    a = False
                    return a
            if root.right:
                if root.right.val <= root.val:
                    a = False
                    return a
                r_minv = max(minv,root.val)
                if not dfs(root.right,r_minv,maxv):
                    a = False
                    return a
            return a
        
        return dfs(root,-1001,1001)


        