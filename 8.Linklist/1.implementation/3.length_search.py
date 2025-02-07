# https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-linked-list

# array to linklist 

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        # code here
        
        if not arr:
            return 
        head = Node(arr[0])
        temp = head
        for val in arr[1:]:
            temp.next = Node(val)
            temp = temp.next
        return head
      

# https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=count-nodes-of-linked-list

#Linked list class
'''class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        temp = head
        cnt = 1 #---imp start from current node ie 1
        while temp.next:
            cnt+=1
            temp = temp.next
            
        return cnt

# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=search-in-linked-list-1664434326

''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        
        temp = head
        
        while temp:   #---imp not temp.next
            if temp.data ==key:
                return True
            temp = temp.next
            
        return False
