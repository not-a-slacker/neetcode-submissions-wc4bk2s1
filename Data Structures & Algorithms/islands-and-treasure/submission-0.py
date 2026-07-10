class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        d = 0
        while q:
            z = len(q)
            for a in range(z):
                (i,j) = q.popleft()
                if (i,j) in seen:
                    continue
                seen.add((i,j))
                grid[i][j] = d
                if i+1 <m:
                    if (i+1,j) not in seen and grid[i+1][j]!=-1:
                        q.append((i+1,j))
                if i-1>=0:
                    if (i-1,j) not in seen and grid[i-1][j]!=-1:
                        q.append((i-1,j))
                if j+1<n:
                    if (i,j+1) not in seen and grid[i][j+1]!=-1:
                        q.append((i,j+1))
                if j-1>=0:
                    if (i,j-1) not in seen and grid[i][j-1]!=-1:
                        q.append((i,j-1))
            d+=1




