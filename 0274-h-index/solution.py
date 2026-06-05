"""
LeetCode 0274 - H-Index
https://leetcode.com/problems/h-index/

Time:  O(n log n)
Space: O(1)
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3, 0, 6, 1, 5]))  # 3
    print(sol.hIndex([1, 3, 1]))  # 1
