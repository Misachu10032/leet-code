# 0211. Design Add and Search Words Data Structure

**Difficulty:** Medium
**Topics:** String, Depth-First Search, Design, Trie
**Link:** https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Approach

Trie, but search is a DFS: a '.' branches into every child.

## Complexity

- Time: O(L) add, O(26^dots * L) search
- Space: O(total characters)

## Follow-ups / gotchas

- Words are at most 25 chars with at most 2 dots, so branching stays small.
