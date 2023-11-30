#Python program to create a FIFO queue.
import queue
q = queue.Queue()

for x in range(4):
    q.put(str(x))

while not q.empty():
    print(q.get(), end=" ")
print("\n")
