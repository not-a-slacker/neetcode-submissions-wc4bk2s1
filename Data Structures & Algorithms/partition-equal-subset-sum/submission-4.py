class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        s=sum(nums)
        if s%2==1:
            return False
        else:
            t = s//2
            dp = []
            for i in range(t+1):
                a = []
                for j in range(n+1):
                    a.append(0)
                dp.append(a)
            for i in range(n+1):
                dp[0][i] = 1
            for j in range(1,n+1):
                for i in range(0,t+1):
                    if i - nums[j-1] >=0:
                        if dp[i-nums[j-1]][j-1]==1:
                            dp[i][j] = 1
                    if dp[i][j-1] ==1:
                        dp[i][j] = 1
            ans = False
            for i in range(n+1):
                if dp[t][i]==1:
                    ans = True
            return ans