# 0117. Populating Next Right Pointers in Each Node II

**Difficulty:** Medium
**Topics:** Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
**Link:** https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

## Approach

Walk each level using the next pointers already set, and build the next level's linked list
with a dummy head + tail. Then jump to dummy.next.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- BFS with a queue is easy but O(n) space; the follow-up wants O(1).
- Not a perfect tree (unlike 116), so children can be missing.
