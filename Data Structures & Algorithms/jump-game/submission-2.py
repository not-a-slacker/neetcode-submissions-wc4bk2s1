class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp = [0]*n
        dp[0]=1
        for i in range(n):
            if dp[i] ==0:
                continue
            j = 1
            while j<=nums[i] and (i+j) < n:
                dp[i+j] = 1
                j+=1
            i += nums[i]+1

        return (dp[-1]==1)
