"""
LeetCode 0019 - Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))  # [1, 2, 3, 5]
    print(to_list(sol.removeNthFromEnd(build([1]), 1)))  # []
    print(to_list(sol.removeNthFromEnd(build([1, 2]), 1)))  # [1]
