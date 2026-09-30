"""
LeetCode 0191 - Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Time:  O(number of set bits)
Space: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))  # 3
    print(sol.hammingWeight(128))  # 1
    print(sol.hammingWeight(2147483645))  # 30
