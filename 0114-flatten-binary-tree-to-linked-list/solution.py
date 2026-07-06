"""
LeetCode 0114 - Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Time:  O(n)
Space: O(1)
"""


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def to_list(root):
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right


if __name__ == "__main__":
    sol = Solution()
    root = build([1, 2, 5, 3, 4, None, 6])
    sol.flatten(root)
    print(to_list(root))  # [1, None, 2, None, 3, None, 4, None, 5, None, 6]
