class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for ch in s:
            if ch.isalnum() and ch!=" ":
                new_s += ch
        rev_s = new_s[::-1]
        if new_s.lower() == rev_s.lower():
            return True
        else:
            return False
        