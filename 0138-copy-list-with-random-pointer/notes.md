# 0138. Copy List with Random Pointer

**Difficulty:** Medium
**Topics:** Hash Table, Linked List
**Link:** https://leetcode.com/problems/copy-list-with-random-pointer/

## Approach

Two passes with a map old -> new. First create all copies, then wire next/random through the map.

## Complexity

- Time: O(n)
- Space: O(n)

## Follow-ups / gotchas

- Putting None -> None in the map removes null checks.
- O(1) space trick: interleave copies (A -> A' -> B -> B'), set randoms, then split.
