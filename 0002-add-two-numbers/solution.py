"""
LeetCode 0002 - Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Time:  O(max(m, n))
Space: O(1) extra
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            cur.next = ListNode(digit)
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    print(to_list(sol.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))))  # [7, 0, 8]
    print(to_list(sol.addTwoNumbers(build([9, 9, 9, 9, 9, 9, 9]), build([9, 9, 9, 9]))))  # [8, 9, 9, 9, 0, 0, 0, 1]
