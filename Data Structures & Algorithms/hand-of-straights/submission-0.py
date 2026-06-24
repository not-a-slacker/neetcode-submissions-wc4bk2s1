class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize != 0:
            return False
        hand.sort()
        print(hand)
        a =n/groupSize
        fc = {}
        for i in hand:
            if fc.get(i):
                fc[i] +=1
            else:
                fc[i] = 1
        print(f"fc : {fc}")
        for i in range(n):
            print(f"fc : {fc}")
            if fc[hand[i]] > 0:
                t = fc[hand[i]]
                for j in range(groupSize):
                    print(f"i {i} ; hand[i] : {hand[i]} ; j : {j}")
                    if not fc.get(hand[i]+j):
                        print("hello")
                        return False
                    if fc[hand[i]+j] < fc[hand[i]]:
                        print("goodbye")
                        return False
                    fc[hand[i]+j] -= t

        return True
            
        