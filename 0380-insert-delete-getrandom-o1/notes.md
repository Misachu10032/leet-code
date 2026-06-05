# 0380. Insert Delete GetRandom O(1)

**Difficulty:** Medium
**Topics:** Array, Hash Table, Math, Design, Randomized
**Link:** https://leetcode.com/problems/insert-delete-getrandom-o1/

## Approach

List for O(1) random access + dict mapping value -> index.
To remove, overwrite the slot with the last element and pop the end.

## Complexity

- Time: O(1) average per op
- Space: O(n)

## Follow-ups / gotchas

- Update the moved element's index before deleting the removed value (handles removing the last element too).
- A set alone can't do O(1) random choice.
