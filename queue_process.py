from collections import deque 

stack = deque()
varias = input()
varias = varias.split()

for i in varias:
    stack.appendleft(str(i))
print(stack)

for i in varias:
    if "o" in i:
        print(i)
        