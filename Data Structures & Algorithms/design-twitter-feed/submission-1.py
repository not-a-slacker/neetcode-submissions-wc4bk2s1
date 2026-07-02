class Twitter:

    def __init__(self):
        self.m1 = {}
        self.m2 = {}
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if self.m1.get(userId):
            self.count +=1
            self.m1[userId].append((self.count,tweetId))
        else:
            self.m1[userId] = []
            self.count+=1
            self.m1[userId].append((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq
        a = []
        res = []
        if not self.m2.get(userId):
            self.m2[userId] = set()
        self.m2[userId].add(userId)
        for b in self.m2[userId]:
            if self.m1.get(b):
                c = self.m1[b][-1]
                heapq.heappush(a,(-c[0],len(self.m1[b])-1,c[1],b))
        while len(a) > 0 and len(res) < 10:
            d = heapq.heappop(a)
            res.append(d[2])
            if d[1] > 0:
                e = self.m1[d[3]][d[1]-1]
                heapq.heappush(a,(-e[0],d[1]-1,e[1],d[3]))
        return res



        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.m2.get(followerId):
            self.m2[followerId] = set()
            self.m2[followerId].add(followerId)
            self.m2[followerId].add(followeeId)
        else:
            self.m2[followerId].add(followeeId)



        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.m2.get(followerId):
            if followeeId in self.m2[followerId]:
                self.m2[followerId].remove(followeeId)
        
        
