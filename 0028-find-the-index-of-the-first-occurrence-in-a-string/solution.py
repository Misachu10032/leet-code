"""
LeetCode 0028 - Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Time:  O(n * m)
Space: O(1)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr('sadbutsad', 'sad'))  # 0
    print(sol.strStr('leetcode', 'leeto'))  # -1
