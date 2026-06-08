
'''
    [cur, prev]
    indegree = [0] * numCourses
    1. adj list -> prev -> {}
        for all edges, add 1 to the cur node indegree[courses[0]] += 1
        
    2. add all indegree = 0 to the deque
    3. while deque
        course = deque.popleft()

        res.append()
        for c in adj[course]:
            indegree[c] -= 1
            if == 0:
                deque.append() 
        

    
    4. if the len(res) != numCourses:
        return []
    else: 
        return res
    
'''

from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        for cur, prev in prerequisites:
            adj[prev].append(cur)
            indegree[cur] += 1
        
        q = deque()
        for i, ind in enumerate(indegree):
            if ind == 0:
                q.append(i)
        
        res = []
        while q:
            course = q.popleft()

            res.append(course)
            for c in adj[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
        
        if len(res) != numCourses:
            return []

        return res
        