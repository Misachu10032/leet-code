"""
LeetCode 0149 - Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Time:  O(n^2)
Space: O(n)
"""


from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        best = 0
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
                best = max(best, slopes[(dx, dy)] + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[1, 1], [2, 2], [3, 3]]))  # 3
    print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # 4
