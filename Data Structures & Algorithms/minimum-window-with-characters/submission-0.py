class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) <len(t):
            return ""
        t_freq = {}
        for ch in t:
            if t_freq.get(ch) is None:
                t_freq[ch] = 1
            else:
                t_freq[ch] += 1
        t_freq1 = t_freq.copy()
        l = 0 
        r = 0
        minLen = 1001
        min_substr = ""
        curr_substr = ""
        partOfSubstr = False
        while r < len(s) :
            if t_freq.get(s[r]) is None and partOfSubstr == False:
                r+=1
                l+=1
                continue
            elif t_freq.get(s[r]) is None:
                r+=1
                continue
            else:
                partOfSubstr = True
                t_freq[s[r]] -=1
                while t_freq.get(s[l]) is None or t_freq.get(s[l]) < 0:
                    if t_freq.get(s[l]) is not None:
                        t_freq[s[l]] +=1
                    l +=1
                found = True
                for ch in t_freq:
                    if t_freq[ch] > 0:
                        found = False
                if found :
                    if r-l+1 <= minLen :
                        min_substr = s[l:r+1]
                        minLen = r-l+1
                r+=1
                # print(f"l : {l} ; r : {r}")
                # print(f"t_freq.get('B') : {t_freq.get('B')}")
                # print(f"t_freq.get('A') : {t_freq.get('A')}")
                # print(f"t_freq.get('C') : {t_freq.get('C')}")
        return min_substr



