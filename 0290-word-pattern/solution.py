"""
LeetCode 0290 - Word Pattern
https://leetcode.com/problems/word-pattern/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        p_to_w, w_to_p = {}, {}
        for p, w in zip(pattern, words):
            if p_to_w.get(p, w) != w or w_to_p.get(w, p) != p:
                return False
            p_to_w[p] = w
            w_to_p[w] = p
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern('abba', 'dog cat cat dog'))  # True
    print(sol.wordPattern('abba', 'dog cat cat fish'))  # False
    print(sol.wordPattern('aaaa', 'dog cat cat dog'))  # False
