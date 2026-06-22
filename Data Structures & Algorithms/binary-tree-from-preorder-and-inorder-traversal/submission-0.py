# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        num_to_ind = {}
        for i in range(len(inorder)):
            num_to_ind[inorder[i]] = i
        def helper(pl,pr,il,ir):
            nonlocal num_to_ind
            print(f"pl : {pl} ; pr : {pr} ; il : {il} ; ir : {ir}")
            if pl==pr:
                return None
            root = TreeNode(val=preorder[pl])
            i = num_to_ind[root.val]
            l_len = i - il
            r_len = ir - i -1
            print(f"i : {i} ; l_len : {l_len} ; r_len : {r_len}")
            if l_len == 0:
                root.left = None
            else:
                root.left = helper(pl+1,pl+1+l_len,il,i)
            if r_len == 0:
                root.right = None
            else:
                root.right = helper(pl+1+l_len,pl+1+l_len+r_len,i+1,ir)
            return root
        root = helper(0,len(preorder),0,len(inorder))
        return root




        