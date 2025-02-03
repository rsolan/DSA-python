from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)

print(queue.popleft())  # Dequeue -> 1
print(queue)  # deque([2, 3])

queue = deque([1, 2, 3])
print(len(queue))  # Output: 3 - size
print(queue[0])  # Front element -> 1
print(queue[-1])  # Rear element -> 3





from queue import Queue

q = Queue()
q.put(1)  # Enqueue
q.put(2)
q.put(3)

print(q.get())  # Dequeue -> 1
print(q.qsize())  # 2


# Lists can be used, but pop(0) is slow (O(n) time complexity).
queue = []
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))  # Dequeue -> 1
print(queue)  # [2, 3]
