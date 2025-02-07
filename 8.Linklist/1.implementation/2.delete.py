https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #  i am standing at node alread y - so idont know prev of this node
        # NODE = 5
        nextnode = node.next.next #9
        node.val = node.next.val #1
        # 5-1-9
        # 1-1-9
        node.next = nextnode


        
        

        
        
'''
def begin():
    if not head:
        print('list empty')
        return
    # temp = head
    head  = head.next
    # temp = None
def end()
    if not head:
        print('list empty')
        return
    if not head.next:
        head = None
        return
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    
del pso 
        temp = self.head
        while temp.next.data != node.data:
            temp = temp.next
        deletednode = temp.next
        temp.next = temp.next.next
        deletednode = None

        return head
        
        '''






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def delete_from_beginning(self):
        """Delete the first node (head) of the list."""
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_from_end(self):
        """Delete the last node (tail) of the list."""
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:  # If there's only one node
            self.head = None
            return
        temp = self.head
        while temp.next.next:  # Traverse to the second last node
            temp = temp.next
        temp.next = None  # Remove the last node

    def delete_from_position(self, position):
        """Delete a node at a given position (0-based index)."""
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.delete_from_beginning()
            return
        temp = self.head
        for _ in range(position - 1):
            if not temp.next:
                print("Position out of range")
                return
            temp = temp.next
        if not temp.next:
            print("Position out of range")
            return
        temp.next = temp.next.next

    def display(self):
        """Print the linked list elements."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_at_tail(10)
ll.insert_at_tail(20)
ll.insert_at_tail(30)
ll.insert_at_tail(40)
ll.display()  # Output: 10 -> 20 -> 30 -> 40 -> None

ll.delete_from_beginning()
ll.display()  # Output: 20 -> 30 -> 40 -> None

ll.delete_from_end()
ll.display()  # Output: 20 -> 30 -> None

ll.delete_from_position(1)  # Delete node at position 1
ll.display()  # Output: 20 -> None
