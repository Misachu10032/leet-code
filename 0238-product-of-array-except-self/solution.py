"""
LeetCode 0238 - Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Time:  O(n)
Space: O(1) extra (output not counted)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
