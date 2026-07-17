class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= (n-1):
            return False
        neighbours = [[] for _ in range(n)]
        for i in range(len(edges)):
            neighbours[edges[i][0]].append(edges[i][1])
            neighbours[edges[i][1]].append(edges[i][0])
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neighbour in neighbours[i]:
                dfs(neighbour)
            return
        dfs(0)
        return len(visited)==n


        
        