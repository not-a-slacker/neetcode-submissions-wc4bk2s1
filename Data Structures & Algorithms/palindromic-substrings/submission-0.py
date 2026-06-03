class Solution:
    def countSubstrings(self, s: str) -> int:
        new_s = "@#"
        for ch in s:
            new_s += ch
            new_s += "#"
        new_s += "$"
        n = len(new_s)
        p = [0]*n
        center = right = 0
        total = 0
        for i in range(1,n-1):
            mirror = 2*center - i
            print(f"center : {center} ; right : {right}")
            if i < right:
                p[i] = min(right-i,p[mirror])
            while(new_s[i+p[i]+1]==new_s[i-p[i]-1]):
                p[i]+=1
            if i + p[i] > right :
                center = i
                right = i + p[i]
        print(f"new_s : {new_s}")
        print(f"p : {p}")
        for i in range(1,n-1):
            if new_s[i] == "#" and p[i]>0:
                total += (p[i] + 1) // 2
            elif new_s[i] != "#":
                total += (p[i] // 2) + 1
        return total
            
            
            