class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freqMap = {}
        for ch in s1:
            if freqMap.get(ch):
                freqMap[ch] +=1
            else:
                freqMap[ch] =1
        l = 0
        r = 0
        freqMap1 = freqMap.copy()
        while r < len(s2):
            if freqMap.get(s2[r]) is None:
                r+=1
                l=r
                freqMap = freqMap1.copy()
            else:
                if freqMap[s2[r]] == 0:
                    while s2[l] != s2[r]:
                        freqMap[s2[l]] += 1
                        l+=1
                    freqMap[s2[l]] += 1
                    l+=1
                else:
                    freqMap[s2[r]] -=1
                    r+=1
                    pal_found = True
                    for key in freqMap :
                        if freqMap[key]!=0:
                            pal_found = False
                    if pal_found :
                        return True
        return False
