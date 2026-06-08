class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = []
        for i in range(len(text1)+1):
            a=[]
            for j in range(len(text2)+1):
                a.append(-1)
            memo.append(a)
        
        def dfs(i,j,s1,s2):
            if memo[i][j] != -1:
                return memo[i][j]
            if i==len(s1):
                memo[i][j] = 0
                return 0
            if j==len(s2):
                memo[i][j] = 0
                return 0
            if s1[i]==s2[j]:
                a = 1 + dfs(i+1,j+1,s1,s2)
            else:
                a = dfs(i+1,j+1,s1,s2)
            memo[i][j] = max(a,dfs(i+1,j,s1,s2),dfs(i,j+1,s1,s2))
            return memo[i][j]
        dfs(0,0,text1,text2)
        print(f"memo : {memo}")
        
        return memo[0][0]
            

        