"""
LeetCode 0023 - Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

Time:  O(N log k)
Space: O(k)
"""


import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = tail = ListNode()
        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))  # [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_list(sol.mergeKLists([])))  # []
