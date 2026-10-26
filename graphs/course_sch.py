from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for nxt in graph[node]:
                if dfs(nxt):
                    return True
            state[node] = 2
            return False

        for i in range(numCourses):
            if state[i] == 0 and dfs(i):
                return False
        return True