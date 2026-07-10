class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        a = set()
        p = set()
        q = deque()
        for i in range(n):
            q.append((0,i))
        for i in range(1,m):
            q.append((i,0))
        while q:
            (i,j)  = q.popleft()
            if (i,j) in p:
                continue
            p.add((i,j))
            if i+1<m and (i+1,j) not in p and heights[i+1][j]>=heights[i][j]:
                q.append((i+1,j))
            if j+1<n and (i,j+1) not in p and heights[i][j+1]>=heights[i][j]:
                q.append((i,j+1))
            if i-1>=0 and (i-1,j) not in p and heights[i-1][j]>=heights[i][j]:
                q.append((i-1,j))
            if j-1>=0 and (i,j-1) not in p and heights[i][j-1]>=heights[i][j]:
                q.append((i,j-1))
        q = deque()
        for i in range(n):
            q.append((m-1,i))
        for i in range(0,m-1):
            q.append((i,n-1))
        while q:
            (i,j)  = q.popleft()
            if (i,j) in a:
                continue
            a.add((i,j))
            if i+1<m and (i+1,j) not in a and heights[i+1][j]>=heights[i][j]:
                q.append((i+1,j))
            if j+1<n and (i,j+1) not in a and heights[i][j+1]>=heights[i][j]:
                q.append((i,j+1))
            if i-1>=0 and (i-1,j) not in a and heights[i-1][j]>=heights[i][j]:
                q.append((i-1,j))
            if j-1>=0 and (i,j-1) not in a and heights[i][j-1]>=heights[i][j]:
                q.append((i,j-1))
        res = []
        for k in p:
            if k in a:
                (i,j) = k
                res.append([i,j])
        return res
        
                  