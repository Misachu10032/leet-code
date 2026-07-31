# 0295. Find Median from Data Stream

**Difficulty:** Hard
**Topics:** Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
**Link:** https://leetcode.com/problems/find-median-from-data-stream/

## Approach

Two heaps: max-heap for the lower half, min-heap for the upper half, sizes balanced (low may have one extra).
Median is the top of low, or the average of both tops.

## Complexity

- Time: O(log n) add, O(1) median
- Space: O(n)

## Follow-ups / gotchas

- Push through low then high so every element in low <= every element in high.
- Follow-up for values in 0..100: bucket counts.
