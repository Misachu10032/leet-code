"""
LeetCode 0025 - Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            first = group_prev.next
            group_prev.next = kth
            group_prev = first


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.reverseKGroup(build([1, 2, 3, 4, 5]), 2)))  # [2, 1, 4, 3, 5]
    print(to_list(sol.reverseKGroup(build([1, 2, 3, 4, 5]), 3)))  # [3, 2, 1, 4, 5]
