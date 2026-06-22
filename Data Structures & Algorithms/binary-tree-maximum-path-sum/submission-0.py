# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            print(f"root.val : {root.val} ; l : {l} ; r : {r}")
            a = max(root.val + l,root.val + r,root.val)
            b = max(root.val+l+r,a)
            max_sum = max(max_sum,b)
            return a
        dfs(root)
        return max_sum
        




        