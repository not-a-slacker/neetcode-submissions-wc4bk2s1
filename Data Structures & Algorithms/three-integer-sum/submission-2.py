class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            target = -nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r :
                if nums[l] + nums[r] == target :
                    triplets.append([nums[i],nums[l],nums[r]])
                    while nums[l] == nums[l+1] and l<r:
                        l+=1
                        if l==len(nums)-1:
                            break
                    l+=1
                elif nums[l] + nums[r] <target :
                    l +=1
                elif nums[l] + nums[r] >target :
                    r-=1
        
        return triplets
                        

                
