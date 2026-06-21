"""
LeetCode 0202 - Happy Number
https://leetcode.com/problems/happy-number/

Time:  O(log n)
Space: O(1)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        slow, fast = n, next_num(n)
        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return fast == 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # True
    print(sol.isHappy(2))  # False
