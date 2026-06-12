"""
LeetCode 0392 - Is Subsequence
https://leetcode.com/problems/is-subsequence/

Time:  O(len(t))
Space: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence('abc', 'ahbgdc'))  # True
    print(sol.isSubsequence('axc', 'ahbgdc'))  # False
