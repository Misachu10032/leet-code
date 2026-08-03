"""
LeetCode 0009 - Palindrome Number
https://leetcode.com/problems/palindrome-number/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))  # False
