from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)

print(queue.popleft())  # Dequeue -> 1
print(queue)  # deque([2, 3])


from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
q.put(3)

print(q.get())  # Dequeue -> 1
print(q.qsize())  # 2



queue = []
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))  # Dequeue -> 1
print(queue)  # [2, 3]
