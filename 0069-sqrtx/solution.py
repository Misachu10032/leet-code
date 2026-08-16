"""
LeetCode 0069 - Sqrt(x)
https://leetcode.com/problems/sqrtx/

Time:  O(log x)
Space: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))  # 2
    print(sol.mySqrt(8))  # 2
    print(sol.mySqrt(0))  # 0
    print(sol.mySqrt(1))  # 1
