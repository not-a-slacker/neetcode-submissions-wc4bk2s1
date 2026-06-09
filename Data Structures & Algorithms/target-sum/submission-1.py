class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = []
        s = sum(nums)
        if target > s:
            return 0
        for i in range(len(nums)+1):
            a=[]
            for j in range(2*s +1):
                a.append(-1)
            dp.append(a)
        # dp --> [len(nums)+1,2*s+1]
        def dfs(i,target):
            print(f"i : {i} ; target : {target}")
            if target > s or target <-s:
                return 0
            
            if dp[i][target + s] != -1:
                return dp[i][target]
            if i==len(nums):
                if target==0:
                    dp[i][target] = 1
                    return dp[i][target]
                else:
                    dp[i][target] = 0
                    return dp[i][target]
            add = target + s - nums[i]
            sub = target + s + nums[i]
            a = 0
            b = 0
            if add >=0 and add < (2*s + 1):
                if dp[i+1][add]!=-1:
                    a += dp[i+1][add]
                else:
                    dp[i+1][add] = dfs(i+1,add-s)
                    a+= dp[i+1][add]
            if sub >=0 and sub < (2*s + 1):
                if dp[i+1][sub]!=-1:
                    b += dp[i+1][sub]
                else:
                    dp[i+1][sub] = dfs(i+1,sub-s)
                    b+= dp[i+1][sub]
            return a + b
        return dfs(0,target)
        


                
                
                

            
        