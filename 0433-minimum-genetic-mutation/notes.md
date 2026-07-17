# 0433. Minimum Genetic Mutation

**Difficulty:** Medium
**Topics:** Hash Table, String, Breadth-First Search
**Link:** https://leetcode.com/problems/minimum-genetic-mutation/

## Approach

BFS where each step changes one character to A/C/G/T, only allowing genes in the bank.

## Complexity

- Time: O(B * L * 4)
- Space: O(B)

## Follow-ups / gotchas

- startGene doesn't need to be in the bank.
- Smaller version of Word Ladder.
