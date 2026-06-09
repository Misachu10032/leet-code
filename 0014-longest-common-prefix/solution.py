"""
LeetCode 0014 - Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Time:  O(S) where S = total characters
Space: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))  # fl
    print(repr(sol.longestCommonPrefix(['dog', 'racecar', 'car'])))  # ''
