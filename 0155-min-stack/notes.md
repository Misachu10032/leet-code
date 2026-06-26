# 0155. Min Stack

**Difficulty:** Medium
**Topics:** Stack, Design
**Link:** https://leetcode.com/problems/min-stack/

## Approach

Store (value, min so far) pairs. The min at the top is always the min of the whole stack.

## Complexity

- Time: O(1) per op
- Space: O(n)

## Follow-ups / gotchas

- Alternative: a second stack that only pushes when val <= current min.
