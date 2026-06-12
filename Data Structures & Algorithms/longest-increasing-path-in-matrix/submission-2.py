class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(-1)
            dp.append(a)
        def dfs(i,j,p):
            if i >= m or i<0 or j >= n or j<0:
                return 0
            if p >= matrix[i][j]:
                return 0
            if i+1 < m and dp[i+1][j]!=-1 and matrix[i][j] < matrix[i+1][j]:
                a = dp[i+1][j]
            else:
                a = dfs(i+1,j,matrix[i][j])
            if j+1 < n and dp[i][j+1]!=-1 and matrix[i][j] < matrix[i][j+1]:
                b = dp[i][j+1]
            else:
                b = dfs(i,j+1,matrix[i][j])
            if j-1 >=0 and dp[i][j-1]!=-1 and matrix[i][j] < matrix[i][j-1]:
                c = dp[i][j-1]
            else:
                c = dfs(i,j-1,matrix[i][j])
            if i-1 >=0 and dp[i-1][j]!=-1 and matrix[i][j] < matrix[i- 1][j]:
                d = dp[i-1][j]
            else:
                d = dfs(i-1,j,matrix[i][j])
            
            dp[i][j] = 1 + max(a,b,c,d)
            return dp[i][j]
        ans = -float('inf')
        for i in range(m):
            for j in range(n):
                z = dfs(i,j,-float('inf'))
                dp[i][j] = z
                if z >= ans:
                    ans = z
        return int(ans)

            
             


        