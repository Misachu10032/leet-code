# 0202. Happy Number

**Difficulty:** Easy
**Topics:** Hash Table, Math, Two Pointers
**Link:** https://leetcode.com/problems/happy-number/

## Approach

The digit-square sequence either reaches 1 or loops. Detect the loop with Floyd's
slow/fast pointers (same idea as linked list cycle).

## Complexity

- Time: O(log n)
- Space: O(1)

## Follow-ups / gotchas

- A seen-set works too, with O(log n) space.
