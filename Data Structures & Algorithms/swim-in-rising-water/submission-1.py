class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        min_heap = [(grid[0][0],0,0)]
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        visited = set()
        while min_heap:
            cost,x,y = heapq.heappop(min_heap)
            visited.add((x,y))
            if x==n-1 and y==n-1:
                return cost
            for i in range(len(dx)):
                    new_x = x+dx[i]
                    new_y = y+dy[i]
                    if new_x >=0 and new_x < n and new_y>=0 and new_y<n and (new_x,new_y) not in visited:
                        visited.add((new_x,new_y))
                        new_cost = max(cost,grid[new_x][new_y])
                        heapq.heappush(min_heap,(new_cost,new_x,new_y))
                    


        