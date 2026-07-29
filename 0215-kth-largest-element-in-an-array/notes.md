# 0215. Kth Largest Element in an Array

**Difficulty:** Medium
**Topics:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

## Approach

Keep a min-heap of the k largest seen so far; its top is the kth largest.

## Complexity

- Time: O(n log k)
- Space: O(k)

## Follow-ups / gotchas

- Quickselect is O(n) average but O(n^2) worst case.
- Counting sort works since values are bounded (-10^4..10^4).
