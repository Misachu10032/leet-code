"""
LeetCode 0209 - Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        best = float("inf")
        total = 0
        l = 0
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if best == float("inf") else best


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
    print(sol.minSubArrayLen(4, [1, 4, 4]))  # 1
    print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
