"""
LeetCode 0039 - Combination Sum
https://leetcode.com/problems/combination-sum/

Time:  O(n^(target / min))
Space: O(target / min)
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))  # [[2, 2, 3], [7]]
    print(sol.combinationSum([2, 3, 5], 8))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(sol.combinationSum([2], 1))  # []
