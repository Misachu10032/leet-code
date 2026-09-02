"""
LeetCode 0015 - 3Sum
https://leetcode.com/problems/3sum/

Time:  O(n^2)
Space: O(1) extra (ignoring sort)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([0, 1, 1]))  # []
    print(sol.threeSum([0, 0, 0]))  # [[0, 0, 0]]
