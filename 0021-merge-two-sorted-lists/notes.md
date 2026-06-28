# 0021. Merge Two Sorted Lists

**Difficulty:** Easy
**Topics:** Linked List, Recursion
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

## Approach

Dummy head + tail pointer. Attach the smaller head each step, then append whatever is left.

## Complexity

- Time: O(m + n)
- Space: O(1)

## Follow-ups / gotchas

- Recursive version is shorter but uses O(m + n) stack.
