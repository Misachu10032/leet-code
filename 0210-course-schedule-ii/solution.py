"""
LeetCode 0210 - Course Schedule II
https://leetcode.com/problems/course-schedule-ii/

Time:  O(V + E)
Space: O(V + E)
"""


from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1, 0]]))  # [0, 1]
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0, 1, 2, 3]
    print(sol.findOrder(2, [[1, 0], [0, 1]]))  # []
