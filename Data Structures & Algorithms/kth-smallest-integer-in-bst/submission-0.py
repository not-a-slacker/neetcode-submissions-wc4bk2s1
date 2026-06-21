# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
num_ch = {}
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count_chil(root):
            if not root:
                return 0
            a = count_chil(root.left)
            b = count_chil(root.right)
            num_ch[root.val] = (a,b)
            return (a+b+1)
        count_chil(root)
        node = root
        while True:
            print(node.val)
            if k <= num_ch[node.val][0]:
                node = node.left
                continue
            if k == num_ch[node.val][0] + 1:
                return node.val
            if k > num_ch[node.val][0] + 1:
                k -= (num_ch[node.val][0] + 1)
                node = node.right
                continue
        
