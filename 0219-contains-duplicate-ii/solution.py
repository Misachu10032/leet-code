"""
LeetCode 0219 - Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last = {}
        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True
            last[num] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
    print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # True
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # False
