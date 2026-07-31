"""
LeetCode 0067 - Add Binary
https://leetcode.com/problems/add-binary/

Time:  O(max(m, n))
Space: O(max(m, n))
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            carry, bit = divmod(total, 2)
            res.append(str(bit))
        return "".join(reversed(res))


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary('11', '1'))  # 100
    print(sol.addBinary('1010', '1011'))  # 10101
