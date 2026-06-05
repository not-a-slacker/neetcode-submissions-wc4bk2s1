class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = [0]*(amount+1)
        a[0] = 0
        for i in range(1,amount+1):
            a[i] = -1
            t = 10001
            for j in coins:
                if i-j>=0:
                    if a[i-j]>-1:
                        t = min(t,a[i-j]+1)
            if t<10001:
                a[i]=t
        
        return a[amount]