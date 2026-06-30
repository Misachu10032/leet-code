# 0025. Reverse Nodes in k-Group

**Difficulty:** Hard
**Topics:** Linked List, Recursion
**Link:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Approach

For each group, find the kth node; if missing, stop (leftover stays as is).
Reverse the group pointing its tail at the next group, then reconnect and move to the next group.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Initialize prev as group_next so the reversed group's tail links forward.
- The old first node becomes the new group_prev.
