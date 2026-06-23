class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        a=[]
        for i in range(n):
            a.append(gas[i]-cost[i])
        if sum(a) < 0:
            return -1
        currSum=0
        currLen=0
        currEnd=-1
        for j in range(2*n):
            i = j%n
            currSum += a[i]
            if currSum < 0:
                currLen=0
                currEnd=-1
                currSum=0
                continue
            currLen+=1
            currEnd=i
            if currLen == n:
                return (i+1) % n
        return -1
            


            
        