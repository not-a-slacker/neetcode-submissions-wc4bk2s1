class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 1
        l = 0
        r = 0
        currChars = [-1] * 200
        currChars[ord(s[l])] = 0
        while r < len(s) - 1:
            r += 1
            while currChars[ord(s[r])] != -1:
                currChars[ord(s[l])] = -1
                l+=1
            currChars[ord(s[r])] = r
            currLen = r - l + 1
            if currLen > maxLen :
                maxLen = currLen
        return maxLen
            

