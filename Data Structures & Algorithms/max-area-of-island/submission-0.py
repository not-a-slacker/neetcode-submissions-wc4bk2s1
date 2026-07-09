class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j,grid,m,n):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return 0
            grid[i][j]=0
            a = dfs(i+1,j,grid,m,n)
            b = dfs(i-1,j,grid,m,n)
            c = dfs(i,j+1,grid,m,n)
            d = dfs(i,j-1,grid,m,n)
            return 1 + a + b + c + d
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxi = max(maxi,dfs(i,j,grid,m,n))
        return maxi

        