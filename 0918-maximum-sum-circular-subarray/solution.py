"""
LeetCode 0918 - Maximum Sum Circular Subarray
https://leetcode.com/problems/maximum-sum-circular-subarray/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = 0
        cur_max = cur_min = 0
        best_max = best_min = nums[0]
        for num in nums:
            cur_max = max(num, cur_max + num)
            best_max = max(best_max, cur_max)
            cur_min = min(num, cur_min + num)
            best_min = min(best_min, cur_min)
            total += num
        if best_max < 0:
            return best_max
        return max(best_max, total - best_min)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # 3
    print(sol.maxSubarraySumCircular([5, -3, 5]))  # 10
    print(sol.maxSubarraySumCircular([-3, -2, -3]))  # -2
