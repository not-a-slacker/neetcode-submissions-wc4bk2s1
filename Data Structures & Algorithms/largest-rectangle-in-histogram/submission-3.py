class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==1:
            return heights[0]
        lStack = []
        rStack = []
        left_sizes = [0] * len(heights)
        right_sizes = [0] * len(heights)
        max_area = 0
        for i in range(len(heights)):
            while len(lStack)>0 and heights[i] <= heights[lStack[-1]]:
                top = lStack.pop()
                left_sizes[i] += left_sizes[top] + 1
            lStack.append(i)
        for i in range(len(heights)-1,-1,-1):
            while len(rStack)>0 and heights[i] <= heights[rStack[-1]]:
                top = rStack.pop()
                right_sizes[i] += right_sizes[top] + 1
            rStack.append(i)
        print(f"left_sizes : {left_sizes}")
        print(f"right_sizes : {right_sizes}")
        for i in range(len(heights)):
            area = (left_sizes[i] + right_sizes[i] + 1)*heights[i]
            max_area = max(max_area,area)
        return max_area
            


            