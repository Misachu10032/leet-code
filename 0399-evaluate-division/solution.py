"""
LeetCode 0399 - Evaluate Division
https://leetcode.com/problems/evaluate-division/

Time:  O(Q * (V + E))
Space: O(V + E)
"""


from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(cur, target, seen):
            if cur == target:
                return 1.0
            seen.add(cur)
            for nxt, weight in graph[cur].items():
                if nxt not in seen:
                    result = dfs(nxt, target, seen)
                    if result != -1.0:
                        return weight * result
            return -1.0

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.calcEquation([['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]))  # [6.0, 0.5, -1.0, 1.0, -1.0]
