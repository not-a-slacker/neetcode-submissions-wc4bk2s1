# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = []
        max = -float('inf')
        def dfs(node,max):
            num = 0
            if not node:
                return 0
            if node.val >= max:
                max = node.val
                num +=1
            if node.right:
                num += dfs(node.right,max)
            if node.left:
                num += dfs(node.left,max)
            return num
        num = dfs(root,max)
        return num
            


        