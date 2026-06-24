"""
LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Time:  O(n log n)
Space: O(1) extra
"""


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arrows = 0
        arrow_x = float("-inf")
        for start, end in points:
            if start > arrow_x:
                arrows += 1
                arrow_x = end
        return arrows


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # 2
    print(sol.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))  # 4
    print(sol.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
