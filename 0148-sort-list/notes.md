# 0148. Sort List

**Difficulty:** Medium
**Topics:** Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
**Link:** https://leetcode.com/problems/sort-list/

## Approach

Merge sort: split at the middle with slow/fast pointers, sort both halves, merge them.

## Complexity

- Time: O(n log n)
- Space: O(log n)

## Follow-ups / gotchas

- Start fast at head.next so a 2-node list splits into 1 + 1 (otherwise infinite recursion).
- True O(1) space needs bottom-up merge sort.
