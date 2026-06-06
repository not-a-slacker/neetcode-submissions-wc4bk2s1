class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        a = [0]*(n+1)
        a[0] = 1
        m = len(wordDict)
        t = 0
        for i in range(m):
            t = max(t,len(wordDict[i]))
        b = set()
        for word in wordDict:
            b.add(word)
        for i in range(n):
            print(f"a : {a}")
            for j in range(t):
                if i-j>=0:
                    print(f"i : {i} ; j : {j}")
                    print(f"s[i-j:i+1]:{s[i-j:i+1]}")
                    if s[i-j:i+1] in b:
                        if a[i-j] ==1:
                            a[i+1] = 1
        print(f"a : {a}")
        return (a[-1]==1)
        