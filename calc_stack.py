from collections import deque 

stack = deque()
varias = input()
varias = varias.split()

for i in varias:
    stack.append(int(i))
print(stack)


for x in range(int(i)):
    p = stack.pop()
    n = p ** 2
    print(n)

