class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a = [0,0]
        for i in range(2,n+1):
            a.append(min(a[-1]+cost[i-1],a[-2]+cost[i-2]))
        return a[n]
        
        