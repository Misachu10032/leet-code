# 0092. Reverse Linked List II

**Difficulty:** Medium
**Topics:** Linked List
**Link:** https://leetcode.com/problems/reverse-linked-list-ii/

## Approach

Walk to the node before `left`. Then repeatedly take the node after `cur` and move it
to the front of the sublist (head insertion), right - left times.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Dummy node handles left == 1.
- `cur` stays the same node the whole time; it drifts to the end of the reversed part.
