class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max = 0
        while l < r :
            curr = (r-l)*min(heights[l],heights[r])
            if curr > max :
                max = curr
            if heights[l] < heights[r] :
                l+=1
            else:
                r-=1
        return max
            