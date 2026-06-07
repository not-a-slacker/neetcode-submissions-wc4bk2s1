from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in nums[1:]:
            if i > dp[-1]:
                dp.append(i)
            else:
                a = bisect_left(dp,i)
                dp[a] = i
        return len(dp)
            