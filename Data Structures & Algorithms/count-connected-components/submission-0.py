class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = [[] for _ in range(n)]
        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for neighbour in neighbours[i]:
                dfs(neighbour)
        count =0
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count
        