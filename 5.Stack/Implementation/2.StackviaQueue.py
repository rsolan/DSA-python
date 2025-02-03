# https://leetcode.com/problems/implement-stack-using-queues/description/

from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q)-1):  #- using 1 queue
            top = self.q[0]
            self.q.append(top)
            self.q.popleft()

    def pop(self) -> int:
        top =  self.q[0]
        self.q.popleft()
        return top
        

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False
          
# m2 - use 2 queue

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        popped_val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

        return popped_val
        
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        top_val = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

        return top_val

    def empty(self) -> bool:
        return len(self.q1) == 0

