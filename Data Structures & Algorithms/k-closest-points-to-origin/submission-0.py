class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math
        a = []
        for i in points:
            d = math.sqrt(i[0]**2 + i[1]**2)
            heapq.heappush(a,(-d,i))
            if len(a) > k:
                heapq.heappop(a)
        b = []
        for i in a:
            b.append(i[1])
        return b
        

        