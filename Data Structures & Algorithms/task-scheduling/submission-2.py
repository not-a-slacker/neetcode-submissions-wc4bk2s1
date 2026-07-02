class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = deque()
        import heapq
        a = []
        f = {}
        for i in tasks:
            if f.get(i):
                f[i] +=1
            else:
                f[i] = 1
        for i in f:
            heapq.heappush(a,[-f[i],i])
        while a or q:
            if a:
                b = heapq.heappop(a)
                b[0] = -b[0]
                print(b)
                time +=1
                if q:
                    if time >= q[0][1]:
                        c = q.popleft()
                        heapq.heappush(a,c[0])
                b[0] -=1
                b[0] = -b[0]
                if b[0]:
                    q.append([b,time+n])
            elif q:
                c = q.popleft()
                print(c)
                time = max(time,c[1])
                heapq.heappush(a,c[0])
        return time

                