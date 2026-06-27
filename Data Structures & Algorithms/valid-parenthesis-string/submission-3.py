class Solution:
    def checkValidString(self, s: str) -> bool:
        a = deque()
        b = deque()
        for i in range(len(s)):
            if s[i]=="(":
                a.append(i)
            elif s[i]==")":
                if len(a)>0:
                    a.pop()
                elif len(b)>0:
                    b.pop()
                else:
                    return False
            elif s[i]=="*":
                b.append(i)
        while len(a) > 0:
            if len(b)==0:
                return False
            c = a.pop()
            d = b.pop()
            if d < c:
                return False
        return True
        




        