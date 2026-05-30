class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        a=[0,nums[0]]
        for i in range(1,n-1):
            a.append(max(a[-1],a[-2]+nums[i]))
        max1 = a[-1]
        a=[0,nums[1]]
        for i in range(2,n):
            a.append(max(a[-1],a[-2]+nums[i]))
        max2 = a[-1]
        return max(max1,max2)




        