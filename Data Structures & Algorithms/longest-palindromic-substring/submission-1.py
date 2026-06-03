class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        max_l = 0
        max_r = 0
        for i in range(n):
            l = i
            r = i
            while l>=0 and r<n:
                if s[l] == s[r]:
                    if (r-l+1)>max_len:
                        max_len = max(max_len,(r-l+1))
                        max_l = l
                        max_r=r
                    l-=1
                    r+=1
                else:
                    break
            
            l=i
            r=i+1
            while l>=0 and r<n:
                if s[l] == s[r]:
                    if (r-l+1)>max_len:
                        max_len = max(max_len,(r-l+1))
                        max_l = l
                        max_r= r
                    l-=1
                    r+=1
                else:
                    break
            
        return s[max_l:max_r+1]

            
