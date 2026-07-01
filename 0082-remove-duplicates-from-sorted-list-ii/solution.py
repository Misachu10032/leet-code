"""
LeetCode 0082 - Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                while cur.next and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.deleteDuplicates(build([1, 2, 3, 3, 4, 4, 5]))))  # [1, 2, 5]
    print(to_list(sol.deleteDuplicates(build([1, 1, 1, 2, 3]))))  # [2, 3]
