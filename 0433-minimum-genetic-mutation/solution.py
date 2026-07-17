"""
LeetCode 0433 - Minimum Genetic Mutation
https://leetcode.com/problems/minimum-genetic-mutation/

Time:  O(B * L * 4)
Space: O(B)
"""


from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        q = deque([(startGene, 0)])
        seen = {startGene}
        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for ch in "ACGT":
                    nxt = gene[:i] + ch + gene[i + 1:]
                    if nxt in bank_set and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, steps + 1))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.minMutation('AACCGGTT', 'AACCGGTA', ['AACCGGTA']))  # 1
    print(sol.minMutation('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']))  # 2
