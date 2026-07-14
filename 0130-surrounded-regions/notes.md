# 0130. Surrounded Regions

**Difficulty:** Medium
**Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
**Link:** https://leetcode.com/problems/surrounded-regions/

## Approach

Reverse thinking: an 'O' survives only if it connects to the border. Flood fill from every
border 'O' marking it safe ('S'), then flip remaining 'O' -> 'X' and 'S' -> 'O'.

## Complexity

- Time: O(m * n)
- Space: O(m * n)

## Follow-ups / gotchas

- Searching from each inner region and checking if it touches the border is messier.
