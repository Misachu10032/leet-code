"""
LeetCode 0055 - Jump Game
https://leetcode.com/problems/jump-game/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
            if farthest >= len(nums) - 1:
                return True
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))  # True
    print(sol.canJump([3, 2, 1, 0, 4]))  # False
