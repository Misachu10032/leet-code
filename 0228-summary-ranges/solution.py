"""
LeetCode 0228 - Summary Ranges
https://leetcode.com/problems/summary-ranges/

Time:  O(n)
Space: O(1) extra
"""


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                res.append(str(start))
            else:
                res.append(f"{start}->{nums[i]}")
            i += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))  # ['0->2', '4->5', '7']
    print(sol.summaryRanges([0, 2, 3, 4, 6, 8, 9]))  # ['0', '2->4', '6', '8->9']
