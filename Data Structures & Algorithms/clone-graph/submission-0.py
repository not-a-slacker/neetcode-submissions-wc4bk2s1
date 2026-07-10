"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        seen = {}
        def dfs(node):
            if node is None:
                return
            n1 = Node(val = node.val)
            seen[node.val] = n1
            for i in node.neighbors:
                if not seen.get(i.val):
                    i1 = dfs(i)
                    n1.neighbors.append(i1)
                else:
                    n1.neighbors.append(seen[i.val])
            return n1
        n = dfs(node)
        return n




                
        