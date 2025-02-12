https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        # code here
        # edit the linked list
        # m1
        temp = head
        while temp:
            if temp.data ==key:
                if temp == head:  #-update head for first case only
                    head = head.next
                    
                nextnode = temp.next
                prevnode = temp.prev
                
                if prevnode:  #--vvimp only update link if they exist
                    prevnode.next = nextnode
                if nextnode:
                    nextnode.prev = prevnode
                    
                temp = nextnode #move forward
    
            else:
                temp= temp.next #move forward
                 
        return head
