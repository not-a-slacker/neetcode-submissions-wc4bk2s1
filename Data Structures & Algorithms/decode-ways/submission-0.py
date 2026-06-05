class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0]*(n+1)
        if int(s[0])==0:
            return 0
        ways[0] = 1
        ways[1] = 1
        for i in range(2,n+1):
            digit = int(s[i-1])
            sl = int(s[i-2])
            if sl ==0 and digit==0:
                ways[i]==0
            if digit!=0:
                ways[i] += ways[i-1]
            if sl==1:
                ways[i] += ways[i-2]
            if sl==2 and digit<7:
                ways[i] += ways[i-2]
        return ways[n]
            
            
            



        