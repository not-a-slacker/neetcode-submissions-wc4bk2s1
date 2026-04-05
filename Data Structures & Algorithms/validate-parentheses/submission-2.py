class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch=="{" or ch=="[":
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif ch ==")":
                top = stack.pop()
                if top != "(":
                    return False
            elif ch =="}":
                top = stack.pop()
                if top != "{":
                    return False
            elif ch =="]":
                top = stack.pop()
                if top != "[":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
            
        