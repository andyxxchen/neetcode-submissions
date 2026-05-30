from collections import defaultdict, deque


'''
    ["hrn","hrf","er","enn","rfnn"]
    n -> f
    h -> e
    r -> n
    e -> r
    f -> {}


    w -> {}
    r -> {}
    t -> {}
    k -> {}

    "zyx","yxw","wvu"

    z -> y
    y -> w
'''
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # store it in adj map
        # do topological sort (Kahn algorithm)
        adj = defaultdict(set)

        for word in words:
            for c in word:
                adj[c]
        


        for w in range(1, len(words)):
            word1 = words[w-1]
            word2 = words[w]

            # invalid
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            
            i, j = 0, 0
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    # edge found
                    adj[word1[i]].add(word2[j])
                    break
                i += 1
                j += 1

        deq = deque()

        # find a indegree = 0 point
        indegree = {u: 0 for u in adj}
        for _, v in adj.items():
            print(_, v)
            for i in v:
                indegree[i] += 1
        
        for u, v in indegree.items(): 
            if v == 0:
                deq.append(u)
        

        res = ""
        # h has no indegree
        while deq:
            cur = deq.popleft()
            res += cur

            for c in adj[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    deq.append(c)
            
        if len(res) != len(adj):
            return ""
        return res