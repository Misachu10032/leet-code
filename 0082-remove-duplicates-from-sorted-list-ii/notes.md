# 0082. Remove Duplicates from Sorted List II

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

## Approach

prev points to the last node we're keeping. When cur starts a run of duplicates,
skip the whole run and link prev past it; otherwise advance prev.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Remove all copies, not just extras (unlike problem 83).
- Dummy head since the first nodes can be removed.
