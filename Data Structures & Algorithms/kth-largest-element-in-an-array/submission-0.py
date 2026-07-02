class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        import heapq
        for i in nums:
            heapq.heappush(a,i)
            if len(a) > k:
                heapq.heappop(a)
        return a[0]
            

        