class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=collections.defaultdict(list)
        tickets.sort(reverse=True)
        for u,v in tickets:
            adj[u].append(v)
        iti = []
        def dfs(i):
            while len(adj[i]):
                j=adj[i].pop()
                dfs(j)
            iti.append(i)
        dfs('JFK')
        return iti[::-1]
            


        