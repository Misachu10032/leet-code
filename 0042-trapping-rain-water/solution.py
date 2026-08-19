"""
LeetCode 0042 - Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
        return water


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))  # 9
