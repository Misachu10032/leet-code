# 0077. Combinations

**Difficulty:** Medium
**Topics:** Backtracking
**Link:** https://leetcode.com/problems/combinations/

## Approach

Backtrack choosing increasing numbers so each combination is generated once.

## Complexity

- Time: O(C(n, k) * k)
- Space: O(k)

## Follow-ups / gotchas

- Prune: stop the loop when there aren't enough numbers left to fill the path.
- Append a copy (path[:]), not path itself.
