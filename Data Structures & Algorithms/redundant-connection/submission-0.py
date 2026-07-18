class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbours = [[] for _ in range(n+1)]
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        visited = set()
        cycle_nodes = set()
        first = -1
        def dfs(src,parent):
            nonlocal first
            if src in visited:
                first = src
                return True
            visited.add(src)
            for neigh in neighbours[src]:
                if neigh==parent:
                    continue
                is_cycle = dfs(neigh,src)
                if first!=-1 and is_cycle:
                    cycle_nodes.add(neigh)
                    return True
                    if first==src:
                        first = -1
                        return False
            return False
        is_cycle = dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle_nodes and v in cycle_nodes:
                return [u,v]
                
                



            


