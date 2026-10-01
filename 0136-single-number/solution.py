"""
LeetCode 0136 - Single Number
https://leetcode.com/problems/single-number/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))  # 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # 4
