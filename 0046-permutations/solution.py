"""
LeetCode 0046 - Permutations
https://leetcode.com/problems/permutations/

Time:  O(n! * n)
Space: O(n)
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    path.append(num)
                    backtrack(path, used)
                    path.pop()
                    used[i] = False

        backtrack([], [False] * len(nums))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(sol.permute([1]))  # [[1]]
