"""
LeetCode 0153 - Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))  # 1
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(sol.findMin([11, 13, 15, 17]))  # 11
