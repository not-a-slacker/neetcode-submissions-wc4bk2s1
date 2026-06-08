class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = []
        for i in range(len(prices)):
            a = []
            for j in range(4): # buy,dont buy,sell,dont sell
                a.append(None)
            memo.append(a)
        def dfs(i,coin):
            if i >= len(prices):
                return 0
            if coin:
                if i==len(prices) - 1:
                    memo[i][2] = prices[i]
                    memo[i][3] = 0
                    return prices[i]
                if memo[i][2] is None:
                    memo[i][2] = prices[i] + dfs(i+2,False)
                if memo[i][3] is None:
                    memo[i][3] = dfs(i+1,True)
                return max(memo[i][2],memo[i][3])
            else:
                if i==len(prices) - 1:
                    memo[i][0] = -prices[i]
                    memo[i][1] = 0
                if memo[i][0] is None:
                    memo[i][0] = dfs(i+1,True) - prices[i]
                if memo[i][1] is None:
                    memo[i][1] = dfs(i+1,False)
                return max(memo[i][0],memo[i][1])
        return dfs(0,False)
                


        