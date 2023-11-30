#Python program to find the three largest integers from a given list of numbers using the heap queue algorithm.
import heapq as hq
nums_list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original list:")
print(nums_list)

largest_nums = hq.nlargest(3, nums_list)
print("\nThree largest numbers are:", largest_nums)
