class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        m = len(wordList[0])
        set_words = set(wordList)
        buckets = collections.defaultdict(list)
        dist = 1
        q = deque()
        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                buckets[pattern].append(word)
        word = beginWord
        for i in range(m):
            pattern = word[:i] + "*" + word[i+1:]
            buckets[pattern].append(word)

        print(f"buckets : {buckets}")
        q.append(beginWord)
        visited = set()
        while q:
            l = len(q)
            for i in range(l):
                curr_word = q.popleft()
                print(f"curr_word : {curr_word}")
                visited.add(curr_word)
                for i in range(m):
                    pattern = curr_word[:i] + "*" + curr_word[i+1:]
                    for neigh in buckets[pattern]:
                        if neigh in visited:
                            continue
                        if neigh == endWord:
                            return dist + 1
                        q.append(neigh)
            dist+=1
        return 0

                





        