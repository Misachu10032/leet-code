"""
LeetCode 0066 - Plus One
https://leetcode.com/problems/plus-one/

Time:  O(n)
Space: O(1) (O(n) when all 9s)
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
    print(sol.plusOne([9]))  # [1, 0]
