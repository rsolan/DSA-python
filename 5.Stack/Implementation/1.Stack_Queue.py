#User function Template for python3
# https://www.geeksforgeeks.org/problems/implement-stack-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-stack-using-array
class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        return self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if len(self.arr) ==0:
            return -1
        else:
            return self.arr.pop()



#User function Template for python3
# https://www.geeksforgeeks.org/problems/implement-queue-using-array/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=implement-queue-using-array
class MyQueue:
    def __init__(self):
        self.arr=[]
        
    #Function to push an element x in a queue.
    def push(self, x):
         return self.arr.append(x)
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
         
         # add code here
         if len(self.arr) == 0:
             return -1
         else:
             return self.arr.pop(0)
