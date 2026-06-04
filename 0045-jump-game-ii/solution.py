"""
LeetCode 0045 - Jump Game II
https://leetcode.com/problems/jump-game-ii/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        cur_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
        return jumps


if __name__ == "__main__":
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))  # 2
    print(sol.jump([2, 3, 0, 1, 4]))  # 2
