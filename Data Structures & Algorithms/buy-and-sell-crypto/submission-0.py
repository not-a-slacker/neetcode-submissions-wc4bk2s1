class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMaxProfit = 0
        buy = 0
        sell = 0
        currMin = 101
        for i in prices:
            if i <currMin:
                currMin = i
            else:
                currMaxProfit = max(currMaxProfit,(i-currMin))
        return currMaxProfit            