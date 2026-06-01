# 1. Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Map
**Link:** https://leetcode.com/problems/two-sum/

## Approach

Single pass with a hash map of value -> index. For each number, check if its
complement (target - num) was already seen; if so, return both indices.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Brute force is O(n^2); the hash map trades space for a single pass.
- Assumes exactly one solution and can't reuse the same element twice.
