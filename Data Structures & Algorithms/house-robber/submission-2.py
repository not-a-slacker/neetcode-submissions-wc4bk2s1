class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == 1:
            return nums[0]
        a = [0,nums[0]]
        for i in range(1,n):
            a.append(max(a[-1],a[-2]+nums[i]))
        return a[-1]
        