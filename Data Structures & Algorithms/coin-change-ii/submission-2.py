class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = []
        for i in range(amount+1):
            a=[]
            for j in range(len(coins)):
                a.append(0)
            dp.append(a)
        for j in range(len(coins)):
            dp[0][j] = 1
        coins = sorted(coins)
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i-coins[j] >=0:
                    #print(f"dp[{i-coins[j]}][{j}] = {dp[i-coins[j]][j]}")
                    dp[i][j] += dp[i-coins[j]][j]
                if j-1 >=0 :
                    #print(f"dp[{i}][{j-1}] = {dp[i][j-1]}")
                    dp[i][j] += dp[i][j-1]
        #print(f"dp : {dp}")
        return dp[amount][len(coins)-1]



        