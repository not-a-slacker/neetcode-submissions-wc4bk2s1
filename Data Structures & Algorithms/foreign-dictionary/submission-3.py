class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        vocab = set()
        for word in words:
            for c in word:
                vocab.add(c)
        adj = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                min_len = min(len(words[i]),len(words[j]))
                if words[i][:min_len] == words[j][:min_len] and len(words[i]) > len(words[j]):
                    return ""
                for k in range(min_len):
                    if words[i][k] != words[j][k] :
                        #print(f"words[i][k] : {words[i][k]} ; words[j][k] : {words[j][k]}")
                        if words[j][k] not in adj[words[i][k]]:
                            indegree[words[j][k]] +=1
                        adj[words[i][k]].add(words[j][k])
                        
                        break
        q = deque()
        for c in vocab:
            if indegree[c]==0:
                q.append(c)
        order = ""
        while q:
            ch = q.popleft()
            print(f"ch : {ch}")
            order+= ch
            # indegree[ch] -=1
            for neigh in adj[ch]:
                indegree[neigh] -=1
                print(f"neigh : {neigh} ; indegree[neigh] : {indegree[neigh]}")
                if indegree[neigh]==0:

                    q.append(neigh)
        for key,value in indegree.items():
            if value > 0:
                return ""
        return order
                
        