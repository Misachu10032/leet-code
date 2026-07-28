"""
LeetCode 0034 - Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        start = lower_bound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, lower_bound(target + 1) - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(sol.searchRange([], 0))  # [-1, -1]
