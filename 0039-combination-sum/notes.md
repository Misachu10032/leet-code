# 0039. Combination Sum

**Difficulty:** Medium
**Topics:** Array, Backtracking
**Link:** https://leetcode.com/problems/combination-sum/

## Approach

Backtrack with a start index so combinations stay non-decreasing (no duplicates).
Recurse with the same i since numbers can be reused.

## Complexity

- Time: O(n^(target / min))
- Space: O(target / min)

## Follow-ups / gotchas

- Sorting lets us break early once a candidate is too big.
- Pass i (not i + 1) to allow reuse.
