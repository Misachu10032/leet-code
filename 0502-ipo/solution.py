"""
LeetCode 0502 - IPO
https://leetcode.com/problems/ipo/

Time:  O(n log n)
Space: O(n)
"""


import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = sorted(zip(capital, profits))
        available = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available, -projects[i][1])
                i += 1
            if not available:
                break
            w -= heapq.heappop(available)
        return w


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # 4
    print(sol.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))  # 6
