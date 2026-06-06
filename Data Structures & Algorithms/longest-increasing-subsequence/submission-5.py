class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2,n+1):
            m = 0
            for j in range(i-1):
                if nums[j] < nums[i-1]:
                    m = max(dp[j+1],m)
            dp[i] = m + 1
        print(f"dp : {dp}")
        return max(dp)