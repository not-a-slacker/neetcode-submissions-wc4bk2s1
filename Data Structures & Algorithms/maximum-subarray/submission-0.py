class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = max(curr_sum+nums[i],nums[i])
            max_sum = max(curr_sum,max_sum)
        return max_sum

        