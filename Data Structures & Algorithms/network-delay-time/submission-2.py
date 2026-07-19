import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
            # edges[v].append((u,w))
        min_heap = [(0,k)]
        dist = [float('inf')]*(n+1)
        dist[k]  = 0
        while len(min_heap):
            curr_dist,node = heapq.heappop(min_heap)
            if dist[node] < curr_dist:
                continue
            
            for neigh,weight in edges[node]:
                if weight + curr_dist < dist[neigh]:
                    dist[neigh] = curr_dist + weight
                    heapq.heappush(min_heap,(weight+curr_dist,neigh))
        max_dist = -float('inf')
        print(f"dist : {dist}")
        for i in range(1,n+1):
            if math.isinf(dist[i]):
                return -1
            max_dist = max(max_dist,dist[i])
        return max_dist


        