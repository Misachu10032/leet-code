"""
LeetCode 0127 - Word Ladder
https://leetcode.com/problems/word-ladder/

Time:  O(N * L^2)
Space: O(N * L^2)
"""


from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                for nxt in patterns[key]:
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
                patterns[key] = []
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))  # 5
    print(sol.ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))  # 0
