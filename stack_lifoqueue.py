from queue import LifoQueue
n=int(input())
stack=LifoQueue(maxsize=n)
print("Initial size",stack.qsize())
for i in range(n):
    stack.put(input())
print("Queue size is",stack.qsize())
if stack.full():
    print("Queue is full")
print(stack.get())
print(stack.get())
print(stack.get())
