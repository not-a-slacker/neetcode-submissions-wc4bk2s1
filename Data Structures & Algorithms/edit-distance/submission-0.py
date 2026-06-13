class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m==0:
            return n
        if n==0:
            return m
        dp = []
        for i in range(m+1):
            a = []
            for j in range(n+1):
                a.append(-1)
            dp.append(a)
        for i in range(n+1):
            dp[0][i] = i
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    a = dp[i-1][j-1]
                else:
                    a = 1 + dp[i-1][j-1]
                b = 1 + dp[i-1][j]
                c = 1 + dp[i][j-1]
                dp[i][j] = min(a,b,c)
        for i in range(m+1):
            print(dp[i])
        return dp[m][n]

            
