#Python program to compute the maximum product of three numbers in a given array of integers using the heap queue algorithm.
import heapq
def maximumProduct(nums):
    
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], b[0] * b[0] * b[1])
arr_nums = [12, 74, 9, 50, 61, 41]
print("Original array elements:")
print(arr_nums)
print("Maximum product of three numbers of the said array:")
print(maximumProduct(arr_nums))
