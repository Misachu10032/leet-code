"""
LeetCode 0137 - Single Number II
https://leetcode.com/problems/single-number-ii/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 3, 2]))  # 3
    print(sol.singleNumber([0, 1, 0, 1, 0, 1, 99]))  # 99
    print(sol.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))  # -4
