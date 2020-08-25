from queue import Queue
n=int(input())
queue=Queue(maxsize=n)
print("Initial size",queue.qsize())
for i in range(n):
    queue.put(input())
print("Queue size is",queue.qsize())
if queue.full():
    print("Queue is full")
print(queue.get())
print(queue.get())
print(queue.get())
if queue.empty():
    print("Queue is empty")
