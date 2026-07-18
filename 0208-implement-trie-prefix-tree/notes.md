# 0208. Implement Trie (Prefix Tree)

**Difficulty:** Medium
**Topics:** Hash Table, String, Design, Trie
**Link:** https://leetcode.com/problems/implement-trie-prefix-tree/

## Approach

Each node has a dict of children and an end-of-word flag. search and startsWith share a walk helper;
search also requires the end flag.

## Complexity

- Time: O(L) per op
- Space: O(total characters)

## Follow-ups / gotchas

- A fixed array of 26 children is faster but uses more memory.
