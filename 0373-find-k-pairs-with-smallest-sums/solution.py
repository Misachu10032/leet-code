"""
LeetCode 0373 - Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Time:  O(k log k)
Space: O(k)
"""


import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # [[1, 2], [1, 4], [1, 6]]
    print(sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # [[1, 1], [1, 1]]
