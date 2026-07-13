# 0200. Number of Islands

**Difficulty:** Medium
**Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
**Link:** https://leetcode.com/problems/number-of-islands/

## Approach

Scan the grid; each unvisited '1' starts a new island. Flood fill (iterative DFS) to sink
the whole island so it isn't counted again.

## Complexity

- Time: O(m * n)
- Space: O(m * n)

## Follow-ups / gotchas

- Mark visited when pushing, not when popping, to avoid duplicates on the stack.
- Union Find also works.
- Grid values are strings '1'/'0', not ints.
