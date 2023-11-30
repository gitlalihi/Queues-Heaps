#Python program to implement heapsort by pushing all values onto a heap and then popping off the smallest values one at a time.
import heapq as hq
def heapsort(input_list):
    h = []
    for i in input_list:
        hq.heappush(h,input_list)
    return [hq.heappop(h) for x in range(len(h))]
input_list=[1,3,45,8,5,0] 
print(heapsort(input_list))
