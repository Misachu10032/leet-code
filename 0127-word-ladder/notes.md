# 0127. Word Ladder

**Difficulty:** Hard
**Topics:** Hash Table, String, Breadth-First Search
**Link:** https://leetcode.com/problems/word-ladder/

## Approach

BFS over words. Precompute wildcard patterns (h*t -> [hot, hit, ...]) so neighbors are found
without comparing every pair of words.

## Complexity

- Time: O(N * L^2)
- Space: O(N * L^2)

## Follow-ups / gotchas

- Answer counts words in the sequence, not edges, so start at 1.
- Clearing a pattern after use avoids re-scanning it.
- Bidirectional BFS is faster.
