import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                nums.append(matrix[i][j])
        low = 0
        high = len(nums) - 1
        while low<=high:
            mid = math.ceil((low + high)/2)
            if nums[mid] == target:
                return True
            elif low >= high:
                return False
            elif nums[mid] > target:
                if high==mid:
                    high-=1
                else:
                    high = mid
            elif nums[mid] < target:
                if low==mid:
                    low+=1
                else:
                    low = mid
            
        return False

        