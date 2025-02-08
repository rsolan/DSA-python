https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop


#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        '''
        # M1 - USE DICT sc - o(n)
        # return the first position of cycle
        d ={}
        temp = head
        pos = 1
        while temp:
            if temp in d:
                oldpos = d[temp]
                return pos - oldpos  # 6-2 = 4
            d[temp] = pos
            pos+=1
            temp =temp.next

        return 0
        '''
        
        # m2 - use tortoise and hare algo - o(n)
        slow  = head
        fast = head
        # lent=0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  #- in cycle ,move slow in the loop and count the length
                lent =1
                slow = slow.next
                while slow!=fast:#- while loop
                    lent+=1
                    slow = slow.next
                    
                return lent

        return 0

