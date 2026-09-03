"""
LeetCode 0300 - Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/

Time:  O(n log n)
Space: O(n)
"""


from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []
        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
    print(sol.lengthOfLIS([7, 7, 7, 7]))  # 1
