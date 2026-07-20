"""
LeetCode 0077 - Combinations
https://leetcode.com/problems/combinations/

Time:  O(C(n, k) * k)
Space: O(k)
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for num in range(start, n - (k - len(path)) + 2):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4, 2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(sol.combine(1, 1))  # [[1]]
