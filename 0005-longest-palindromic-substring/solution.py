"""
LeetCode 0005 - Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Time:  O(n^2)
Space: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            for l, r in (expand(i, i), expand(i, i + 1)):
                if r - l > end - start:
                    start, end = l, r
        return s[start:end + 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome('babad'))  # bab
    print(sol.longestPalindrome('cbbd'))  # bb
