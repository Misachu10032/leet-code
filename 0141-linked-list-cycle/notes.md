# 0141. Linked List Cycle

**Difficulty:** Easy
**Topics:** Hash Table, Linked List, Two Pointers
**Link:** https://leetcode.com/problems/linked-list-cycle/

## Approach

Floyd's tortoise and hare: fast moves 2 steps, slow moves 1. If there's a cycle they meet.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Seen-set of nodes works but is O(n) space.
- Compare nodes by identity, not value.
