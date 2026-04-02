class Solution:
    def trap(self, height: List[int]) -> int:
        lefts =[]
        rights =[]
        l_max =0
        for i in range(len(height)):
            lefts.append(l_max)
            if height[i] > l_max:
                l_max = height[i]
        r_max = 0
        for i in range(len(height)):
            rights.append(r_max)
            if height[-i-1] > r_max:
                r_max = height[-i-1]
        rights = rights[::-1]
        max_trap = 0
        for i in range(len(height)):
            max_trap += max(0,min(lefts[i],rights[i])-height[i])
        return max_trap
        