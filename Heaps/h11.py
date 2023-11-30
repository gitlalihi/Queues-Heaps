#Python program to check if the letters in a given string can be rearranged. This is to make sure that two characters that are adjacent to each other are different using the heap queue algorithm
import heapq

def rearrange_string(input_str):
    char_freq = {}
    heap = []

    
    for char in input_str:
        char_freq[char] = char_freq.get(char, 0) + 1

    
    for char, freq in char_freq.items():
        heapq.heappush(heap, (-freq, char))

    result = []
    prev_char = None

    while heap:
        freq, char = heapq.heappop(heap)
        
        
        result.append(char)
        if prev_char:
            heapq.heappush(heap, (prev_char[0], prev_char[1]))

       
        if freq < -1:
            heapq.heappush(heap, (freq + 1, char))

        
        prev_char = (freq, char)

    
    return ''.join(result) if len(result) == len(input_str) else None


input_string = "aab"
result = rearrange_string(input_string)

if result:
    print(f"A valid rearrangement: {result}")
else:
    print("No valid rearrangement possible.")
