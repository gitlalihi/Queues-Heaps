#Python function that accepts an arbitrary list and converts it to a heap using the heap queue algorithm.
import heapq as hq
raw_heap = [25, 44, 68, 21, 39, 23, 89]
print("Raw Heap: ", raw_heap)
hq.heapify(raw_heap)
print("\nHeapify(heap): ", raw_heap)
