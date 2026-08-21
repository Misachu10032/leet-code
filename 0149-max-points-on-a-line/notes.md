# 0149. Max Points on a Line

**Difficulty:** Hard
**Topics:** Array, Hash Table, Math, Geometry
**Link:** https://leetcode.com/problems/max-points-on-a-line/

## Approach

For each anchor point, group the other points by slope. The biggest group + the anchor
is the best line through that anchor.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Follow-ups / gotchas

- Store slopes as reduced (dx, dy) pairs, not floats, to avoid precision issues.
- Normalize the sign so (1, 2) and (-1, -2) match.
- Vertical lines are just dx = 0.
