"""
LeetCode 0011 - Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            best = max(best, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(sol.maxArea([1, 1]))  # 1
