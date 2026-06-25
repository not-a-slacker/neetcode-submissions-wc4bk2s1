class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fl = {}
        for i in range(len(s)):
            if not fl.get(s[i]):
                fl[s[i]] = [i,i]
                continue
            fl[s[i]][1]=i
        curr = set()
        a = []
        subs = ""
        for i in range(len(s)):
            subs += s[i]
            curr.add(s[i])
            b = True
            for j in curr:
                if fl[j][1] > i:
                    b = False
                    break
            if b:
                a.append(len(subs))
                subs=""
                curr=set()
        return a




                

        