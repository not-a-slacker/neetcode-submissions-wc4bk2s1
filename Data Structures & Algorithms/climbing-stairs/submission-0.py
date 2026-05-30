class Solution:
    def climbStairs(self, n: int) -> int:
        a = []
        a.append(1)
        a.append(1)
        if n==1:
            return 1
        for i in range(2,n+1):
            a.append(a[-1]+a[-2])
        return a[n]



        