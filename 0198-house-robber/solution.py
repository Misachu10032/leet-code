"""
LeetCode 0198 - House Robber
https://leetcode.com/problems/house-robber/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, cur = 0, 0
        for num in nums:
            prev, cur = cur, max(cur, prev + num)
        return cur


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))  # 4
    print(sol.rob([2, 7, 9, 3, 1]))  # 12
