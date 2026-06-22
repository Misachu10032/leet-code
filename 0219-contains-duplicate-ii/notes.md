# 0219. Contains Duplicate II

**Difficulty:** Easy
**Topics:** Array, Hash Table, Sliding Window
**Link:** https://leetcode.com/problems/contains-duplicate-ii/

## Approach

Remember the last index of each value. A repeat within k of the last index is a hit.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Sliding-window set of size k gives O(k) space.
