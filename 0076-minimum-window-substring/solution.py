"""
LeetCode 0076 - Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Time:  O(m + n)
Space: O(alphabet)
"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        start, end = 0, 0
        l = 0
        for r, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing == 0:
                while need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                if end == 0 or r - l < end - start:
                    start, end = l, r
                need[s[l]] += 1
                missing += 1
                l += 1
        return s[start:end]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow('ADOBECODEBANC', 'ABC'))  # BANC
    print(sol.minWindow('a', 'a'))  # a
    print(repr(sol.minWindow('a', 'aa')))  # ''
