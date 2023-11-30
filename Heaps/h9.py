#Python program to find the top k integers that occur the most frequently from a given list of sorted and distinct integers using the heap queue algorithm.
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    
    heap = []

    
    counter = Counter(nums)

    
    for num, freq in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            
            current_element = (freq, num)
            smallest_element = heap[0]
            if current_element > smallest_element:
                heapq.heappushpop(heap, current_element)

    
    result = [element[1] for element in sorted(heap, key=get_frequency, reverse=True)]

    return result

def get_frequency(element):
    return element[0]


numbers = [4, 4, 4, 2, 2, 3, 1, 1, 5, 5, 5, 5]
k = 2
result = top_k_frequent(numbers, k)
print(f"The {k} most frequent elements are:", result)
