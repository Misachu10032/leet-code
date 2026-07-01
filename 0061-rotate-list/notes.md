# 0061. Rotate List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Link:** https://leetcode.com/problems/rotate-list/

## Approach

Get the length and tail. k %= length. The new tail is at index length - k - 1;
cut there and attach the old tail to the old head.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- k can be much bigger than the length - always mod.
- Same idea as rotate array.
