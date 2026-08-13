"""
LeetCode 0135 - Candy
https://leetcode.com/problems/candy/

Time:  O(n)
Space: O(n)
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


if __name__ == "__main__":
    sol = Solution()
    print(sol.candy([1, 0, 2]))  # 5
    print(sol.candy([1, 2, 2]))  # 4
