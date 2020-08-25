from collections import deque
queue=deque()
n=int(input())
for i in range(n):
    queue.append(input())
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
