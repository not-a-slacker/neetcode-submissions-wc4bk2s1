import heapq
class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        self.median = -100001
        

    def addNum(self, num: int) -> None:
        if len(self.l)==0 and len(self.r)==0:
            heapq.heappush(self.r,num)
            self.median = num
        else:
            if len(self.l) == len(self.r):
                if num >= self.median:
                    heapq.heappush(self.r,num)
                    t = self.r[0]
                    self.median = t
                else:
                    heapq.heappush(self.l,-num)
                    t = heapq.heappop(self.l)
                    t = -t
                    self.median = t
                    heapq.heappush(self.r,t)
            elif len(self.l) + 1 == len(self.r):
                if num >= self.median:
                    heapq.heappush(self.r,num)
                    t = heapq.heappop(self.r)
                    heapq.heappush(self.l,-t)
                    self.median = (-self.l[0] + self.r[0]) /2
                else:
                    heapq.heappush(self.l,-num)
                    self.median = (-self.l[0] + self.r[0]) /2

    def findMedian(self) -> float:
        return self.median
        
        