"""
LeetCode 0530 - Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Time:  O(n)
Space: O(h)
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        best = float("inf")
        prev = None

        def inorder(node):
            nonlocal best, prev
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.getMinimumDifference(build([4, 2, 6, 1, 3])))  # 1
    print(sol.getMinimumDifference(build([1, 0, 48, None, None, 12, 49])))  # 1
