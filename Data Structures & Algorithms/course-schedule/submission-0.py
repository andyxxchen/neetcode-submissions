# 对于 Course Schedule：

# * DFS = 检测回边（back edge）
# * BFS = 拓扑排序（Kahn Algorithm），不断把入度为 0 的 node 加入队列，然后每次访问队列，去消耗这个入度为 0 的


# [[0,1]]
'''

    0 <- 1

    adj = {
        1: [0]
    }

    indegree = [1, 0]

'''

from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # cur_course -> [prerequist]
        # 1. create a indegree list -> index(course num), slot value(num of indegree)
        # 2. initialize a deque, push all 0 indegree index into the deque
        # 3. while deque, look it up in prerequist list, for loop traverse list -1 to all indegree , if 0 push it into the deque
        # 4. while end, if there are some indegree > 0, False else True
        adj = defaultdict(list) # adj list pre -> [list of courses]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        deq = deque()
        for idx, inde in enumerate(indegree):
            if inde == 0:
                deq.append(idx)

        cnt = 0
        while deq:
            cur = deq.popleft()
            cnt += 1

            dependecies = adj[cur] # a list
            for dep in dependecies:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    deq.append(dep)

        if cnt != numCourses:
            return False
        return True
                
                
            


            





        