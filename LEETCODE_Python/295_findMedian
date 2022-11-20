import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower,-heappushpop(self.higher,num))
        if len(self.lower) > len(self.higher):
            heapq.heappush(self.higher,-(heapq.heappop(self.lower)))

    def findMedian(self) -> float:         
        if len(self.lower) < len(self.higher):
                return self.higher[0]
        return (self.lower[0]*-1 + self.higher[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()