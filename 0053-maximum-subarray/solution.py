"""
LeetCode 0053 - Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = current = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(sol.maxSubArray([1]))  # 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))  # 23
