# 0055. Jump Game

**Difficulty:** Medium
**Topics:** Array, Greedy, Dynamic Programming
**Link:** https://leetcode.com/problems/jump-game/

## Approach

Greedy: track the farthest index reachable so far.
Walk left to right; if the current index is beyond `farthest`, we are stuck.
Otherwise extend `farthest` with `i + nums[i]`. Early exit once the last index is reachable.

## Complexity

- Time: O(n)
- Space: O(1)

## Follow-ups / gotchas

- DP (mark each index reachable) works but is O(n^2).
- Alternative: walk backwards keeping a `goal` index; if `i + nums[i] >= goal`, move goal to i.
- A 0 only matters if you can't jump over it.
