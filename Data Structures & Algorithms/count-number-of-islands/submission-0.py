class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j,grid,cid,m,n):
            if i < 0 or i >= m or j <0 or j >= n or grid[i][j]=="0":
                return 
            if grid[i][j] == "1":
                grid[i][j] = cid
                dfs(i+1,j,grid,cid,m,n)
                dfs(i,j+1,grid,cid,m,n)
                dfs(i-1,j,grid,cid,m,n)
                dfs(i,j-1,grid,cid,m,n)
            
            return

            
        m = len(grid)
        n = len(grid[0])
        cid = 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                elif grid[i][j] == "1":
                    dfs(i,j,grid,cid,m,n)
                    cid +=1
        return cid - 2

        