"""
LeetCode 0151 - Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.reverseWords('the sky is blue')))  # 'blue is sky the'
    print(repr(sol.reverseWords('  hello world  ')))  # 'world hello'
