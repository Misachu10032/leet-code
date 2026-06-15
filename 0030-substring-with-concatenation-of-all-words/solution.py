"""
LeetCode 0030 - Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Time:  O(n * word_len)
Space: O(number of words)
"""


from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        count = len(words)
        need = Counter(words)
        res = []
        for offset in range(word_len):
            l = offset
            seen = Counter()
            used = 0
            for r in range(offset, len(s) - word_len + 1, word_len):
                word = s[r:r + word_len]
                if word not in need:
                    seen.clear()
                    used = 0
                    l = r + word_len
                    continue
                seen[word] += 1
                used += 1
                while seen[word] > need[word]:
                    seen[s[l:l + word_len]] -= 1
                    used -= 1
                    l += word_len
                if used == count:
                    res.append(l)
                    seen[s[l:l + word_len]] -= 1
                    used -= 1
                    l += word_len
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.findSubstring('barfoothefoobarman', ['foo', 'bar'])))  # [0, 9]
    print(sol.findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']))  # []
    print(sorted(sol.findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the'])))  # [6, 9, 12]
