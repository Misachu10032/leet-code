# 0212. Word Search II

**Difficulty:** Hard
**Topics:** Array, String, Backtracking, Trie, Matrix
**Link:** https://leetcode.com/problems/word-search-ii/

## Approach

Put all words in a trie, then backtrack from every cell walking the trie at the same time.
Store the full word at its end node so we can collect it directly.

## Complexity

- Time: O(m * n * 4^L)
- Space: O(total characters)

## Follow-ups / gotchas

- Pop the word once found to avoid duplicates.
- Prune empty trie branches after visiting - huge speedup on big inputs.
- Mark the cell '#' while it's on the path.
