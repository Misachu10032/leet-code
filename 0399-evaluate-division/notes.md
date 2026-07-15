# 0399. Evaluate Division

**Difficulty:** Medium
**Topics:** Array, String, Depth-First Search, Breadth-First Search, Union Find, Graph, Shortest Path
**Link:** https://leetcode.com/problems/evaluate-division/

## Approach

Model a / b = v as weighted edges a -> b (v) and b -> a (1/v).
Each query is a path search; multiply the weights along the path.

## Complexity

- Time: O(Q * (V + E))
- Space: O(V + E)

## Follow-ups / gotchas

- Unknown variables return -1.0 even for x / x.
- Weighted Union Find is the faster alternative for many queries.
