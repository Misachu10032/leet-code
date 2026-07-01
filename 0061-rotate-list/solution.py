"""
LeetCode 0061 - Rotate List
https://leetcode.com/problems/rotate-list/

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.rotateRight(build([1, 2, 3, 4, 5]), 2)))  # [4, 5, 1, 2, 3]
    print(to_list(sol.rotateRight(build([0, 1, 2]), 4)))  # [2, 0, 1]
