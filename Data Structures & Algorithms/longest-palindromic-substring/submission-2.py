class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_s = "%#"
        for ch in s:
            new_s += ch
            new_s += "#"
        new_s += "$"
        n = len(new_s)
        print(f"n : {n} ; new_s : {new_s}")
        p = [0]*n
        center = right = 0
        for i in range(1,n-1):
            mirror = 2*center - i
            print(f"center : {center} ; right : {right}")
            if i<right:
                p[i] = min(right - i,p[mirror])
            while (new_s[i+p[i]+1]==new_s[i-p[i]-1]):
                p[i]+=1
            if i+p[i]>right:
                center = i
                right = i+p[i]
        max_r = 0
        max_center = 0
        for i in range(n):
            if p[i] > max_r:
                max_r = p[i]
                max_center = i
        s = new_s[max_center-max_r:max_center+max_r + 1]
        t = ""
        for ch in s:
            if ch != "#" and ch != "%" and ch!= "$":
                t += ch
        return t