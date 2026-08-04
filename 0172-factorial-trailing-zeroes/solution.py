"""
LeetCode 0172 - Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))  # 0
    print(sol.trailingZeroes(5))  # 1
    print(sol.trailingZeroes(0))  # 0
    print(sol.trailingZeroes(100))  # 24
