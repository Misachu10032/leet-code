# 0167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Binary Search
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Approach

Sorted input: start at both ends. Sum too small -> move left up, too big -> move right down.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Answer is 1-indexed.
- Hash map works too but needs O(n) space.
