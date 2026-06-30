# 0019. Remove Nth Node From End of List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Approach

One pass: move fast n + 1 ahead, then move both until fast is None. Slow is right before the target.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Dummy node handles removing the head.
- Two-pass version: count length, then walk length - n.
