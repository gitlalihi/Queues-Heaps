#Python program to find the nth super ugly number from a given prime list of size k using the heap queue algorithm.
import heapq

def nthSuperUglyNumber(n, primes):
   
    ugly_numbers = [1]
    heap = primes[:]
    
   
    heapq.heapify(heap)
    seen = set(primes)
    
    for _ in range(1, n):
        current_min = heapq.heappop(heap)
        ugly_numbers.append(current_min)
        
        for prime in primes:
            next_ugly = prime * current_min
            if next_ugly not in seen:
                seen.add(next_ugly)
                heapq.heappush(heap, next_ugly)

    return ugly_numbers[-1]


n = 12
primes = [2, 7, 13, 19]
result = nthSuperUglyNumber(n, primes)
print(f"The {n}th super ugly number is: {result}")
