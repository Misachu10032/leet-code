# 0046. Permutations

**Difficulty:** Medium
**Topics:** Array, Backtracking
**Link:** https://leetcode.com/problems/permutations/

## Approach

Backtracking with a used[] array: at each position try every number not used yet.

## Complexity

- Time: O(n! * n)
- Space: O(n)

## Follow-ups / gotchas

- Swap-based version permutes in place without the used array.
- With duplicates (47), sort and skip equal unused neighbors.
