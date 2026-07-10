class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        t = 2
        while q:
            for a in range(len(q)):
                (i,j) = q.popleft()
                if (i,j) in seen:
                    continue
                grid[i][j] = t
                seen.add((i,j))
                if i+1<m:
                    if grid[i+1][j]==1 and (i+1,j) not in seen:
                        q.append((i+1,j))
                if j+1<n:
                    if grid[i][j+1]==1 and (i,j+1) not in seen:
                        q.append((i,j+1))
                if i-1>=0:
                    if grid[i-1][j]==1 and (i-1,j) not in seen:
                        q.append((i-1,j))
                if j-1>=0:
                    if grid[i][j-1]==1 and (i,j-1) not in seen:
                        q.append((i,j-1))
            t +=1
        maxi = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
                maxi = max(maxi, grid[i][j])

        
        return max(0,maxi -2)
                
                

        