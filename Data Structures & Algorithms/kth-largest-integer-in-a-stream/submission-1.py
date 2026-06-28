class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
            if i>=k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


        
