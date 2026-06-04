# 0045. Jump Game II

**Difficulty:** Medium
**Topics:** Array, Greedy, Dynamic Programming
**Link:** https://leetcode.com/problems/jump-game-ii/

## Approach

Implicit BFS by levels. `cur_end` is the edge of the current level (indices reachable
with `jumps` jumps). While scanning that level, track `farthest` reachable.
When we hit `cur_end`, we must take another jump, and the next level ends at `farthest`.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- Loop to `len(nums) - 1`, not the end, otherwise you count an extra jump when already at the last index.
- Problem guarantees the end is reachable, so no stuck check needed.
- DP `dp[i] = min jumps to i` is O(n^2).
