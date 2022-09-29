# from collections import deque
# stack = deque([])
# stack.append("A")
# stack.append("B")
# stack.append("C")
# stack.append("D")
# print("Initial Stack: ", list(stack))

# for i in range(4):
#     print(stack.pop())

from queue import LifoQueue
stack = LifoQueue()
stack.put("A")
stack.put("B")
stack.put("C")
stack.put("D")
print("Initial Stack Size: ", stack.qsize())
print("Initial Stack Full: ", stack.full())
print("Initial Stack: ", stack.queue)
for i in range(4):
    print(stack.get())
    print(stack.empty())




