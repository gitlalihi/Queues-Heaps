#Python program that adds integer numbers from the data stream to a heapq and computes the median of all elements. Use the heap queue algorithm.
import heapq

class MedianFinder:
    def __init__(self):
        
        self.left_heap = []
        self.right_heap = []

    def add_num(self, num):
        
        if not self.left_heap or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)

        
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def find_median(self):
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2.0
        else:
            return -self.left_heap[0]


median_finder = MedianFinder()
data_stream = [1, 2, 3, 4, 5]

for num in data_stream:
    median_finder.add_num(num)

median = median_finder.find_median()
print(f"Median: {median}")
