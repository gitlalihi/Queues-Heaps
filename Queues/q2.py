#Python program to find out whether a queue is empty or not.
import queue
p = queue.Queue()
q = queue.Queue()
for x in range(4):
    q.put(x)
print(p.empty())
print(q.empty())
