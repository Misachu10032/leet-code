"""
LeetCode 0017 - Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Time:  O(4^n * n)
Space: O(n)
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            for ch in letters[digits[i]]:
                path.append(ch)
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations('23'))  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    print(sol.letterCombinations(''))  # []
    print(sol.letterCombinations('2'))  # ['a', 'b', 'c']
