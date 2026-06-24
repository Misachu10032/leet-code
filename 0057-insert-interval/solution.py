"""
LeetCode 0057 - Insert Interval
https://leetcode.com/problems/insert-interval/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        start, end = newInterval
        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])
        res.extend(intervals[i:])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1, 3], [6, 9]], [2, 5]))  # [[1, 5], [6, 9]]
    print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1, 2], [3, 10], [12, 16]]
