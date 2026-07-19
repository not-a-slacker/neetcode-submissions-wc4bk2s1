class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        n= len(points)
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        res = 0
        min_heap = [(0,0)]
        visited = set()
        while len(visited) < n:
            #print(f"min_heap : {min_heap}")
            dist,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            res += dist
            for weight,neigh in adj[node]:
                if neigh not in visited:
                    heapq.heappush(min_heap,(weight,neigh))
        return res


        