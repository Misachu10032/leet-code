# 0011. Container With Most Water

**Difficulty:** Medium
**Topics:** Array, Two Pointers, Greedy
**Link:** https://leetcode.com/problems/container-with-most-water/

## Approach

Start with the widest container. Always move the shorter wall inward -
moving the taller one can never increase the area.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Brute force is O(n^2).
