"""
LeetCode 0162 - Find Peak Element
https://leetcode.com/problems/find-peak-element/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))  # 2
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 5
