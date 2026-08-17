"""
LeetCode 0050 - Pow(x, n)
https://leetcode.com/problems/powx-n/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))  # 1024.0
    print(round(sol.myPow(2.1, 3), 5))  # 9.261
    print(sol.myPow(2.0, -2))  # 0.25
