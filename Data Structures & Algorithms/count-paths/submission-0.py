class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp  = []
        for i in range(m):
            a=[]
            for j in range(n):
                a.append(0)
            dp.append(a)
        for i in range(m):
            dp[i][0] = 1
        for j in range(1,n):
            for i in range(m):
                if i - 1 >=0:
                    dp[i][j] += dp[i-1][j]
                dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]



        
        