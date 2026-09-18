"""
LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Time:  O(n)
Space: O(w)
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque([root] if root else [])
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.zigzagLevelOrder(build([3, 9, 20, None, None, 15, 7])))  # [[3], [20, 9], [15, 7]]
