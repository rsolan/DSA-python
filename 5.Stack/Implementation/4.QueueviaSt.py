# https://leetcode.com/problems/implement-queue-using-stacks/description/
# m2 - use 2 stacks - but top adn pop are expesnvei not push 
# push - o(1) , pop/top = o(n)
class MyQueue:

    def __init__(self):
        self.s1 =[]
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2)!= 0: 
            return self.s2.pop()
        else:
            while self.s1: #transfer from s1 to s2
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        

    def peek(self) -> int:
        if len(self.s2)!= 0:
            return self.s2[-1]
        else:
            while self.s1: #transfer from s1 to s2
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        

    def empty(self) -> bool:
        if len(self.s1) ==0 and len(self.s2) ==0 :  #- if any one of stack has el - then que is not empty
            return True
        else:
            return False


'''
# m1 - using 2 stack - push is expensive - o(2n)
class MyQueue:

    def __init__(self):
        self.s1 =[]
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()   #this is same as front of queue
        

    def peek(self) -> int:
        top = self.s1[-1]
        return top
        

    def empty(self) -> bool:
        if len(self.s1) ==0:
            return True
        else:
            return False

# use 2 stacks 
# 1. s1 to s2
# 2. x to s1
# 3. s2 back to s1
'''
# push in q - 4 2 3 5

# s1 - 3 2 4
# s2 =[]

# s1 =[x]
# s2 - 4 2 3

# s1 = [x 3 2 4]

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
