"""
LeetCode 0167 - Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            if total < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(sol.twoSum([2, 3, 4], 6))  # [1, 3]
