"""
LeetCode 0139 - Word Break
https://leetcode.com/problems/word-break/

Time:  O(n * L)
Space: O(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        lengths = {len(w) for w in words}
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for length in lengths:
                if length <= i and dp[i - length] and s[i - length:i] in words:
                    dp[i] = True
                    break
        return dp[len(s)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak('leetcode', ['leet', 'code']))  # True
    print(sol.wordBreak('applepenapple', ['apple', 'pen']))  # True
    print(sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))  # False
