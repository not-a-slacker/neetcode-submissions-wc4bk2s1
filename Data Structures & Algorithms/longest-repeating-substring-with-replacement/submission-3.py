class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count_in_current_window = [0] * 26
        l = 0
        r = 0 
        currChanges = 0
        max_len = 1
        char_count_in_current_window[ord(s[l])-ord('A')] = 1
        while r < len(s):
            if r == len(s) - 1:
                return max_len
            r+=1
            char_count_in_current_window[ord(s[r])-ord('A')] +=1
            if (r - l + 1) - max(char_count_in_current_window) <= k :
                max_len = max(max_len,r-l+1)
            while (r - l + 1) - max(char_count_in_current_window) > k :
                char_count_in_current_window[ord(s[l])-ord('A')] -=1
                l+=1

        return max_len

                
            

        