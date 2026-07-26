"""
LeetCode 0035 - Search Insert Position
https://leetcode.com/problems/search-insert-position/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
