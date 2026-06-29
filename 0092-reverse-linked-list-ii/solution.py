"""
LeetCode 0092 - Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

Time:  O(n)
Space: O(1)
"""


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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)))  # [1, 4, 3, 2, 5]
    print(to_list(sol.reverseBetween(build([5]), 1, 1)))  # [5]
