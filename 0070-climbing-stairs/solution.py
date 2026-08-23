"""
LeetCode 0070 - Climbing Stairs
https://leetcode.com/problems/climbing-stairs/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # 2
    print(sol.climbStairs(3))  # 3
    print(sol.climbStairs(5))  # 8
