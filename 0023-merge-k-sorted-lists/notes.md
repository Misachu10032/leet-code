# 0023. Merge k Sorted Lists

**Difficulty:** Hard
**Topics:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

## Approach

Min-heap holding the current head of each list. Pop the smallest, append it, push its next.

## Complexity

- Time: O(N log k)
- Space: O(k)

## Follow-ups / gotchas

- Include the list index in the tuple so ties never compare ListNode objects.
- Divide and conquer (pairwise merging) is also O(N log k).
