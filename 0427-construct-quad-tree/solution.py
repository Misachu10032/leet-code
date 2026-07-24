"""
LeetCode 0427 - Construct Quad Tree
https://leetcode.com/problems/construct-quad-tree/

Time:  O(n^2 log n)
Space: O(log n)
"""


class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def to_nested(node):
    if node.isLeaf:
        return int(node.val)
    return [to_nested(node.topLeft), to_nested(node.topRight),
            to_nested(node.bottomLeft), to_nested(node.bottomRight)]


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        def helper(r, c, size):
            first = grid[r][c]
            if all(grid[i][j] == first for i in range(r, r + size) for j in range(c, c + size)):
                return Node(bool(first), True)
            half = size // 2
            return Node(True, False,
                        helper(r, c, half), helper(r, c + half, half),
                        helper(r + half, c, half), helper(r + half, c + half, half))

        return helper(0, 0, len(grid))


if __name__ == "__main__":
    sol = Solution()
    print(to_nested(sol.construct([[0, 1], [1, 0]])))  # [0, 1, 1, 0]
    print(to_nested(sol.construct([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]])))  # [1, [0, 0, 1, 1], 1, 0]
