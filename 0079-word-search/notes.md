# 0079. Word Search

**Difficulty:** Medium
**Topics:** Array, String, Backtracking, Depth-First Search, Matrix
**Link:** https://leetcode.com/problems/word-search/

## Approach

DFS from every cell matching the word char by char. Temporarily mark the cell '#' so it isn't reused,
then restore it on the way back.

## Complexity

- Time: O(m * n * 3^L)
- Space: O(L)

## Follow-ups / gotchas

- Pruning: if the board doesn't have enough of some letter, return False early.
- Reversing the word when its last letter is rarer speeds it up.
