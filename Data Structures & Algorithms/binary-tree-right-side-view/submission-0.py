# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        if root is None:
            return []
        ans = []
        while q:
            a = False
            b = len(q)
            for i in range(b):
                if not a:
                    c = q.popleft()
                    ans.append(c.val)
                    a = True
                    if c.right:
                        q.append(c.right)
                    if c.left:
                        q.append(c.left)
                else:  
                    c= q.popleft() 
                    if c.right:
                        q.append(c.right)
                    if c.left:
                        q.append(c.left)
        return ans 
