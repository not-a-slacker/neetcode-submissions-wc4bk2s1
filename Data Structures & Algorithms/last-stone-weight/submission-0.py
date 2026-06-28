class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        a = []
        for i in stones:
            a.append(-i)
        heapq.heapify(a)
        while len(a)>1:
            b = heapq.heappop(a)
            c = heapq.heappop(a)
            b = -b
            c = -c
            if b != c:
                heapq.heappush(a,-abs(b-c))
        if len(a)==1:
            return -a[0]
        else:
            return 0
