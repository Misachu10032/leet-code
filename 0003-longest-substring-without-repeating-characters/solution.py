"""
LeetCode 0003 - Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time:  O(n)
Space: O(min(n, alphabet))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        best = 0
        l = 0
        for r, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= l:
                l = last_seen[ch] + 1
            last_seen[ch] = r
            best = max(best, r - l + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(sol.lengthOfLongestSubstring('bbbbb'))  # 1
    print(sol.lengthOfLongestSubstring('pwwkew'))  # 3
