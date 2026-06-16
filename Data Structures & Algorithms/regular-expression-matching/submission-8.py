class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = []
        for i in range(m):
            a=[]
            for j in range(n):
                a.append(-1)
            dp.append(a)
        b = 0
        for i in p:
            if i=="*":
                b+=1
        a = m - n + 2*b
        if a <0:
            return False
        def dfs(i,j):
            #print(f"(i,j):({i},{j})")
            if i==m and j==n:
                return 1
            if j >= n or i > m:
                return 0
            if i<m and j<n and dp[i][j] != -1:
                return dp[i][j]
            # if i==m-1 and j==n-2 and n>=2 and p[n-1] == "*":
            #     if s[i] == p[j] or p[j]==".":
            #         dp[i][j] = 1
            #         return 1
            # if i==m-1 and j==n-1:
            #     if s[i]==p[j]:
            #         dp[i][j] = 1
            #         return 1
            #     elif p[j]==".":
            #         dp[i][j] = 1
            #         return 1
            #     else:
            #         dp[i][j]=0
            #         return 0
            a = -1
            b = -1
            if i==m:
                return dfs(i,j+2)
            if j+1 <=n-1 and p[j+1] == "*":
                if i<m and (s[i]==p[j] or p[j]=="."):
                    a = dfs(i+1,j)
                b = dfs(i,j+2)
                if a==1 or b==1:
                    dp[i][j]=1
                    return dp[i][j]
            elif s[i]==p[j] or p[j]==".":
                dp[i][j] = dfs(i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j] = 0
                return 0
                
        dfs(0,0)
        for i in dp:
            print(i)
        return (dp[0][0]==1)


                

            
                        
                



