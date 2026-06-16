class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = []
        for i in range(n+1):
            a = []
            for j in range(n+1):
                a.append(0)
            dp.append(a)
        for m in range(0,n):
            for l in range(1,n+1):
                r = l + m 
                if r > n:
                    break
                o = -float('inf')
                if l==r:
                    dp[l][r] = nums[l]*nums[l-1]*nums[l+1]
                    continue
                for i in range(l,r+1):
                    p = nums[i]*nums[l-1]*nums[r+1]
                    if i-1 >=l:
                        p += dp[l][i-1]
                    if i+1 <= r:
                        p += dp[i+1][r]
                    o = max(o,p)
                dp[l][r] = o
        for i in dp:
            print(i)
        return dp[1][n]
        
        
        