class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        currMax = 1
        currMin = 1
        for i in range(n):
            t = currMax*nums[i]
            u = currMin*nums[i]
            currMax = max(t,u,nums[i])
            if currMax > ans:
                ans = currMax
            currMin = min(t,u,nums[i])

        return ans
        
        
        