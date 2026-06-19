# 0205. Isomorphic Strings

**Difficulty:** Easy
**Topics:** Hash Table, String
**Link:** https://leetcode.com/problems/isomorphic-strings/

## Approach

Mapping must be one-to-one, so keep maps in both directions and check consistency for each pair.

## Complexity

- Time: O(n)
- Space: O(alphabet)

## Follow-ups / gotchas

- One map isn't enough: 'badc' -> 'baba' passes a one-way check but is invalid.
