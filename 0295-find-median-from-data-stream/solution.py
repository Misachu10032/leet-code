"""
LeetCode 0295 - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Time:  O(log n) add, O(1) median
Space: O(n)
"""


import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap (negated) for the smaller half
        self.high = []  # min-heap for the larger half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0
