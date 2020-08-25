stack=[]
n=int(input())
for i in range(n):
    stack.append(input())
print("Elements in the stack")
print(stack)
top=stack[n-1]
print("Top is",top)
print(stack.pop())
print(stack.pop())
print(stack.pop())
