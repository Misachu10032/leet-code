# 0909. Snakes and Ladders

**Difficulty:** Medium
**Topics:** Array, Breadth-First Search, Matrix
**Link:** https://leetcode.com/problems/snakes-and-ladders/

## Approach

BFS over square numbers (shortest path, each die roll = 1 move).
Convert square -> (row, col) accounting for the boustrophedon layout, and follow snakes/ladders.

## Complexity

- Time: O(n^2)
- Space: O(n^2)

## Follow-ups / gotchas

- Rows are numbered from the bottom and alternate direction.
- Only follow one snake/ladder per move (no chaining).
