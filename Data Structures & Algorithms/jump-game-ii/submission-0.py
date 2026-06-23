class Solution:
    def jump(self, nums: List[int]) -> int:
        dests={}
        dests[0]=0
        curr = 0
        for i in range(len(nums)):
            while i > dests[curr]:
                curr +=1
            dests[curr+1] = max(dests.get(curr+1,0),i + nums[i])
            if dests[curr] >= len(nums) - 1:
                return curr
            if dests[curr+1] >= len(nums) - 1:
                return curr+1
            


            

        