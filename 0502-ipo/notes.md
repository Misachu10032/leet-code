# 0502. IPO

**Difficulty:** Hard
**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)
**Link:** https://leetcode.com/problems/ipo/

## Approach

Sort projects by capital. Each round, push every project we can now afford into a max-heap
of profits, then take the most profitable one.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Follow-ups / gotchas

- Python heapq is a min-heap - store negative profits.
- Stop early if nothing is affordable.
