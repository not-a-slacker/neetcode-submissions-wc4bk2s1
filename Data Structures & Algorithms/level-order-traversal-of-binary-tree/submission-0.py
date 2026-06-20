# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root is None:
            return []
        q.append(root)
        ans = []
        while q:
            b = []
            c = len(q)
            for i in range(c):
                a = q.popleft()
                l = a.left
                r = a.right
                if l:
                    q.append(l)
                if r:
                    q.append(r)
                b.append(a.val)
            ans.append(b)
            print(f"q : {q}")
        print(ans)
        return ans

