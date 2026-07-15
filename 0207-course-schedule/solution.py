"""
LeetCode 0207 - Course Schedule
https://leetcode.com/problems/course-schedule/

Time:  O(V + E)
Space: O(V + E)
"""


from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0
        while q:
            node = q.popleft()
            taken += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return taken == numCourses


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # False
