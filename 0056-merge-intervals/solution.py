"""
LeetCode 0056 - Merge Intervals
https://leetcode.com/problems/merge-intervals/

Time:  O(n log n)
Space: O(n)
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
    print(sol.merge([[1, 4], [4, 5]]))  # [[1, 5]]
