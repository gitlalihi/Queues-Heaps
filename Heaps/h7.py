#Python program to find the kth (1 <= k <= array's length) largest element in an unsorted array using the heap queue algorithm.
import heapq

def find_kth_largest(nums, k):
   
    heap = []

    for num in nums[:k]:
        heapq.heappush(heap, num)

   
    for num in nums[k:]:
        
        heapq.heappushpop(heap, num)

   
    return heap[0]

numbers = [12, 45, 7, 23, 56, 89, 34, 67, 21]
k = 3
result = find_kth_largest(numbers, k)
print(f"The {k}th largest element is:", result)
