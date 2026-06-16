# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertNode(orig):
            if orig == None:
                return None
            cop = copy.deepcopy(orig)
            if cop.left != None:
                cop.left = invertNode(cop.left)
            if cop.right != None:
                cop.right = invertNode(cop.right)
            orig.left = cop.right
            orig.right = cop.left
            return orig
        
        return invertNode(root)


               