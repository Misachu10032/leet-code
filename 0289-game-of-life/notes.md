# 0289. Game of Life

**Difficulty:** Medium
**Topics:** Array, Matrix, Simulation
**Link:** https://leetcode.com/problems/game-of-life/

## Approach

In-place with 2 bits per cell: bit 0 = current state, bit 1 = next state.
Count neighbors using `& 1`, set bit 1 for cells alive next round, then shift everything right.

## Complexity

- Time: O(m * n)
- Space: O(1)

## Follow-ups / gotchas

- Must not overwrite current states while still counting neighbors - that's why the second bit.
- Infinite board follow-up: store only live cells in a set.
