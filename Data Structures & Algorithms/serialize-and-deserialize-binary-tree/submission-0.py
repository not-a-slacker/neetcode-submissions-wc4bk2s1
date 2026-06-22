# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = ""
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                s += "null"
                s += ","
                continue
            s += str(node.val)
            s += ","
            q.append(node.left)
            q.append(node.right)
        if s[-1] == ",":
            s = s[:-1]
        print(f"s : {s}")
        return s
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        a = data.split(",")
        print(f"a : {a}")
        node = TreeNode(val=int(a[0]))
        root = node
        q = deque()
        q.append(node)
        r = deque(a[1:])
        while q:
            node = q.popleft()
            l = r.popleft()
            m = r.popleft()
            if l =="null":
                node.left = None
            else:
                b = TreeNode(val=int(l))
                node.left = b
                q.append(b)
            if m =="null":
                node.right = None
            else:
                c = TreeNode(val=int(m))
                node.right = c
                q.append(c)
        return root

            

        
