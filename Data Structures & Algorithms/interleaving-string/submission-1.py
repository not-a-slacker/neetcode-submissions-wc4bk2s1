class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a = len(s1)
        b = len(s2)
        c = len(s3)
        if a+b != c:
            return False
        dp = []
        for i in range(a + 1):
            d = []
            for j in range(b+1):
                d.append(0)
            dp.append(d)
        dp[0][0] = 1
        for i in range(1,a+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = 1
            else:
                break
        for i in range(1,b+1):
            if s2[i-1] == s3[i-1]:
                dp[0][i] = 1
            else:
                break
        for i in range(1,a+1):
            for j in range(1,b+1):
                if s1[i-1] == s3[i + j -1] and dp[i-1][j] == 1:
                    dp[i][j] = 1
                if s2[j-1] == s3[i+j-1] and dp[i][j-1] ==1:
                    dp[i][j] =1
        
        return (dp[a][b] == 1)
            
        
        

        