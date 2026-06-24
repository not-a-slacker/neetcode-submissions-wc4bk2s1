class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a1 = False
        a2 = False
        a3 = False
        n= len(triplets)
        for i in range(n):
            if triplets[i][0]==target[0] and triplets[i][1] <=target[1] and triplets[i][2]<=target[2]:
                a1=True
            if triplets[i][1]==target[1] and triplets[i][0] <=target[0] and triplets[i][2]<=target[2]:
                a2=True
            if triplets[i][2]==target[2] and triplets[i][0] <=target[0] and triplets[i][1]<=target[1]:
                a3=True
        return (a1 and a2 and a3)
        