class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [0]*(n+1)
    def find(self,v):
        if v!=self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if (px==py):
            return False
        if self.size[px] < self.size[py]:
            px,py = py,px
        self.size[px] += self.size[py]
        self.parent[py] = px
        return True
            
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges=[]
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist,i,j))
        edges.sort()
        res = 0
        c = 0
        for edge in edges:
            dist,i,j = edge
            if dsu.union(i,j):
                res += dist
                c +=1
            if c==(n-1):
                return res
        return res
        
            

        




        
        