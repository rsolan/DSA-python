https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=linked-list-insertion

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        node = Node(x)
        if not head:
            head = node
            return head
            
        temp = head
        while temp.next:
            temp = temp.next
            
        temp.next = node
        
        return head
        
    def athead():
        node = Node(val)
        if not head:
            head = node
        node.next = head
        head = node
        
    def atpos():
        temp = head
        if pos ==1:
            return insertathead
        # if pos == n:
        #     return insertatatil
        for i in range(1,pos-1):
            temp = temp.next
        node.next = temp.next
        temp.next = node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Insert a new node at the beginning (head) of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        """Insert a new node at the end (tail) of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, position):
        """Insert a new node at a given position (0-based index)."""
        new_node = Node(data)
        if position == 0:
            self.insert_at_head(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        """Print the linked list elements."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_head(10)  # Insert at head
ll.insert_at_tail(30)  # Insert at tail
ll.insert_at_position(20, 1)  # Insert at position 1
ll.display()  # Output: 10 -> 20 -> 30 -> None
