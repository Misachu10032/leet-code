"""
LeetCode 0190 - Reverse Bits
https://leetcode.com/problems/reverse-bits/

Time:  O(1) (32 iterations)
Space: O(1)
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(43261596))  # 964176192
    print(sol.reverseBits(2147483644))  # 1073741822
