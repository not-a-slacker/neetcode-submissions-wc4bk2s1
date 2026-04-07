class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0]*len(temperatures)
        for i in range(len(temperatures)):
            elePopped = 0
            if len(stack) > 0:
                print(f"stack[-1][0] : {stack[-1][0]} ; temperatures[len(temperatures) - i - 1] : {temperatures[len(temperatures) - i - 1]}")
            while len(stack) > 0 and stack[-1][0] <= temperatures[len(temperatures) - i - 1]:
                a = stack.pop()
                elePopped += a[1]
                print(f"a[0] : {a[0]} ; a[1] : {a[1]} ; elePopped : {elePopped}")
            if len(stack) == 0:
                results[len(temperatures)-i-1] = 0
            else:
                results[len(temperatures)-i-1] =elePopped + 1
            stack.append((temperatures[len(temperatures) - i - 1],elePopped+1))
        
        return results