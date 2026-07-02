# 0086. Partition List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Link:** https://leetcode.com/problems/partition-list/

## Approach

Build two lists (< x and >= x) with dummy heads, preserving order, then join them.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Set after.next = None or the last node may still point back into the list (cycle).
