"""
LeetCode 0058 - Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Time:  O(n)
Space: O(1)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord('Hello World'))  # 5
    print(sol.lengthOfLastWord('   fly me   to   the moon  '))  # 4
