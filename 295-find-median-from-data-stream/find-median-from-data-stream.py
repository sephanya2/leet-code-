import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # max heap (store negative values)
        self.large = []  # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Step 1: push into max heap
        heapq.heappush(self.small, -num)

        # Step 2: make sure every element in small <= every element in large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: balance sizes
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0