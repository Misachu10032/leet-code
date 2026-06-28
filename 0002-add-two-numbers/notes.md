# 0002. Add Two Numbers

**Difficulty:** Medium
**Topics:** Linked List, Math, Recursion
**Link:** https://leetcode.com/problems/add-two-numbers/

## Approach

Digits are stored in reverse, so add like grade-school addition from the head, carrying over.

## Complexity

- Time: O(max(m, n))
- Space: O(1) extra

## Follow-ups / gotchas

- Keep looping while carry is non-zero (999 + 1).
- Dummy head avoids special-casing the first node.
